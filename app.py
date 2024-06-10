from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/service_list")
def service_list():
    return render_template("service_list.html")


@app.route('/service/<name>')
def service(name):
    return render_template("service.html", service_name=name)