from flask import Flask, render_template, request, redirect,session,send_file
from resume_generator import generate_resume
import json
app = Flask(__name__)
app.secret_key = "portfolio_secret_123"
def load_data():
    with open("data.json", "r") as file:
        return json.load(file)

def save_data(data):
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

portfolio_config = {
    "show_about": True,
    "show_skills": True,
    "show_projects": True,
    "show_certifications": True,
    "show_publications": True,
    "show_achievements": True,
    "show_experience": False,
    "show_languages":True,
    "show_strengths":True
}

@app.route("/")
def home():

    data = load_data()

    return render_template(
    "index.html",
    config=portfolio_config,
    about=data["about"],
    skills=data["skills"],
    projects=data["projects"],
    publications=data["publications"],
    certifications=data["certifications"],
    achievements=data["achievements"],
    experience=data["experience"],
    objective=data["objective"],
    education=data["education"],
    languages=data["languages"],
    strengths=data["strengths"]
)


@app.route("/admin", methods=["GET", "POST"])
def admin():
    if not session.get("admin"):
        return redirect("/login")
    if request.method == "POST":

        portfolio_config["show_about"] = "show_about" in request.form
        portfolio_config["show_skills"] = "show_skills" in request.form
        portfolio_config["show_projects"] = "show_projects" in request.form
        portfolio_config["show_certifications"] = "show_certifications" in request.form
        portfolio_config["show_publications"] = "show_publications" in request.form
        portfolio_config["show_achievements"] = "show_achievements" in request.form
        portfolio_config["show_experience"] = "show_experience" in request.form
        portfolio_config["show_languages"] = "show_languages" in request.form
        portfolio_config["show_strengths"] = "show_strengths" in request.form

        return redirect("/")

    data = load_data()

    return render_template  (
        "admin.html",
        config=portfolio_config,
        projects=data["projects"],
        publications=data["publications"],
        certifications=data["certifications"],
        achievements=data["achievements"],
        experience=data["experience"],
        objective=data["objective"],
        education=data["education"],
        languages=data["languages"],
        strengths=data["strengths"]
    )

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username == "admin" and password == "admin123":
            session["admin"] = True
            return redirect("/admin")

        return "Invalid Username or Password"

    return render_template("login.html")

@app.route("/logout")
def logout():

    session.pop("admin", None)

    return redirect("/")

@app.route("/download-resume")
def download_resume():

    data = load_data()

    pdf_path = generate_resume(data)

    return send_file(
        pdf_path,
        as_attachment=True
    )

@app.route("/update-about", methods=["POST"])
def update_about():

    data = load_data()

    data["about"]["name"] = request.form.get("name", "")
    data["about"]["title"] = request.form.get("title", "")
    data["about"]["description"] = request.form.get("description", "")

    save_data(data)

    return redirect("/")

@app.route("/update-skills", methods=["POST"])
def update_skills():

    data = load_data()

    skills_text = request.form["skills"]

    data["skills"] = skills_text.split(",")

    save_data(data)

    return redirect("/")

@app.route("/add-project", methods=["POST"])
def add_project():

    data = load_data()

    project = {
        "title": request.form["title"],
        "description": request.form["description"]
    }

    data["projects"].append(project)

    save_data(data)

    return redirect("/")

@app.route("/delete-project/<int:index>")
def delete_project(index):
    data = load_data()

    if index < len(data["projects"]):
        data["projects"].pop(index)

    save_data(data)

    return redirect("/")   

@app.route("/add-publication", methods=["POST"])
def add_publication():

    data = load_data()

    data["publications"].append({
        "title": request.form["title"]
    })

    save_data(data)

    return redirect("/")

@app.route("/delete-publication/<int:index>")
def delete_publication(index):
    
    data = load_data()

    if index < len(data["publications"]):
        data["publications"].pop(index)

    save_data(data)

    return redirect("/")
   
@app.route("/add-certification", methods=["POST"])
def add_certification():

    data = load_data()

    data["certifications"].append({
        "title": request.form["title"]
    })

    save_data(data)

    return redirect("/")

@app.route("/delete-certification/<int:index>")
def delete_certification(index):
    data = load_data()

    if index < len(data["certifications"]):
        data["certifications"].pop(index)

    save_data(data)

    return redirect("/")

@app.route("/add-achievement", methods=["POST"])
def add_achievement():

    data = load_data()

    data["achievements"].append({
        "title": request.form["title"]
    })

    save_data(data)

    return redirect("/")

@app.route("/delete-achievement/<int:index>")
def delete_achievement(index):

    data = load_data()

    if index < len(data["achievements"]):
        data["achievements"].pop(index)

    save_data(data)

    return redirect("/")

@app.route("/add-experience", methods=["POST"])
def add_experience():

    data = load_data()

    data["experience"].append({
        "company": request.form["company"],
        "role": request.form["role"]
    })

    save_data(data)

    return redirect("/")

@app.route("/delete-experience/<int:index>")
def delete_experience(index):
    data = load_data()

    if index < len(data["experiences"]):
        data["experiences"].pop(index)

    save_data(data)

    return redirect("/")

@app.route("/add-education", methods=["POST"])
def add_education():

    data = load_data()

    education = {
        "degree": request.form["degree"],
        "college": request.form["college"],
        "cgpa": request.form["cgpa"]
    }

    data["education"].append(education)

    save_data(data)

    return redirect("/")

@app.route("/update-objective", methods=["POST"])
def update_objective():

    data = load_data()

    data["objective"] = request.form["objective"]

    save_data(data)

    return redirect("/")

@app.route("/add-language", methods=["POST"])
def add_language():

    data = load_data()

    language = request.form["language"]

    data["languages"].append(language)

    save_data(data)

    return redirect("/")

@app.route("/delete-language/<int:index>")
def delete_language(index):

    data = load_data()

    del data["languages"][index]

    save_data(data)

    return redirect("/")

@app.route("/add-strength", methods=["POST"])
def add_strength():

    data = load_data()

    strength = request.form["strength"]

    data["strengths"].append(strength)

    save_data(data)

    return redirect("/")

@app.route("/delete-strength/<int:index>")
def delete_strength(index):

    data = load_data()

    del data["strengths"][index]

    save_data(data)

    return redirect("/")
   

@app.route("/update-contact", methods=["POST"])
def update_contact():

    data = load_data()

    data["about"]["email"] = request.form.get("email", "")
    data["about"]["phone"] = request.form.get("phone", "")
    data["about"]["github"] = request.form.get("github", "")
    data["about"]["linkedin"] = request.form.get("linkedin", "")

    save_data(data)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)