from flask import Flask, render_template, request

app = Flask(__name__)

projects = [
    {
        "name": "Job Application Tracker API",
        "slug": "job-application-tracker-api",
        "description": "A REST API for creating, updating, and tracking job applications.",
        "technologies": ["Python", "Flask", "SQLite", "REST API"],
        "image": "1.png",
        "github": "https://github.com/YOUR-USERNAME/job-application-tracker-api",
        "demo": "#",
        "problem": "Job applications can become difficult to organise when applications, interview stages, contacts, and follow-up dates are tracked manually.",
        "solution": "I built an API that allows users to create, update, retrieve, and delete job application records through HTTP requests.",
        "learning": "This project helped me understand HTTP methods, REST API design, routing, validation, database operations, and error handling."
    },
    {
        "name": "Data Analysis Project",
        "slug": "data-analysis-project",
        "description": "A Python project for analysing and visualising real-world data.",
        "technologies": ["Python", "Pandas", "Matplotlib"],
        "image": "2.png",
        "github": "#",
        "demo": "#",
        "problem": "Raw datasets can contain patterns that are difficult to understand without cleaning and visualisation.",
        "solution": "I cleaned and analysed a dataset and created visualisations to communicate the results.",
        "learning": "This project helped me practise data cleaning, analysis, visualisation, and communicating technical findings."
    },
    {
        "name": "Automation Project",
        "slug": "automation-project",
        "description": "A Python tool that automates a repetitive task.",
        "technologies": ["Python", "Automation", "CLI"],
        "image": "3.png",
        "github": "#",
        "demo": "#",
        "problem": "A repetitive manual task was taking unnecessary time.",
        "solution": "I created a Python utility to automate the workflow.",
        "learning": "This project helped me practise Python scripting, file handling, and designing reusable utilities."
    },
    {
        "name": "Weather API",
        "slug": "weather-api",
        "description": "An API that retrieves and processes weather information.",
        "technologies": ["Python", "Flask", "REST API"],
        "image": "4.png",
        "github": "#",
        "demo": "#",
        "problem": "Applications often need a simple way to retrieve structured weather information.",
        "solution": "I created an API that retrieves and exposes weather data in a structured format.",
        "learning": "This project helped me understand API requests, JSON responses, HTTP status codes, and error handling."
    },
]



@app.route("/")
def home():
    return render_template("index.html", projects=projects)

@app.route("/projects/<slug>")
def project_detail(slug):

    for project in projects:
        if project["slug"] == slug:
            return render_template("project.html", project=project)

    return "Project not found", 404

@app.route("/contact", methods=["POST"])
def contact():

    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()

    errors = []

    if not name:
        errors.append("Name is required.")

    if not email:
        errors.append("Email is required.")
    elif "@" not in email:
        errors.append("Please enter a valid email address.")

    if not message:
        errors.append("Message is required.")

    if len(message) > 2000:
        errors.append("Message must be 2000 characters or fewer.")

    if errors:
        return render_template(
            "contact_result.html",
            title="Message not sent",
            label="ERROR",
            errors=errors
        ), 400

    print("New contact message:")
    print("Name:", name)
    print("Email:", email)
    print("Message:", message)

    return render_template(
        "contact_result.html",
        title="Message received",
        label="SUCCESS",
        message="Thank you for your message! I'll get back to you as soon as possible."
    )

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)