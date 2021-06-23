from app import app
from flask import render_template

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html", index=True)

@app.route("/about")
def about():
    return render_template("about.html", about=True)

@app.route("/projects")
@app.route("/projects/<proj>") # <proj> is a variable which can be passed to the page function below along with its default
def projects(proj="2019"):
    courseData = [{"courseID":"1111","title":"PHP 101","description":"Intro to PHP","credits":3,"term":"Fall, Spring"}, {"courseID":"2222","title":"Java 1","description":"Intro to Java Programming","credits":4,"term":"Spring"}, {"courseID":"3333","title":"Adv PHP 201","description":"Advanced PHP Programming","credits":3,"term":"Fall"}, {"courseID":"4444","title":"Angular 1","description":"Intro to Angular","credits":3,"term":"Fall, Spring"}, {"courseID":"5555","title":"Java 2","description":"Advanced Java Programming","credits":4,"term":"Fall"}]
    print(courseData)
    return render_template("projects.html", courseData=courseData, projects=True, proj=proj)

@app.route("/contact")
def contact():
    return render_template("contact.html", login=True, contact=True)