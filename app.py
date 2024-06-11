from flask import Flask, render_template, request, url_for, flash
from dotenv import load_dotenv
import os
from openai import OpenAI
from service_config import service_config
load_dotenv()

# initialise flask
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

# create OpenAI client
OPENAI_KEY = os.environ.get("OPENAI_KEY")
open_ai_client = OpenAI(
    api_key=OPENAI_KEY
)

# function to call OpenAI chat
def query_open_ai(prompt, ai_role, outputs=3): 
    completion = open_ai_client.chat.completions.create(
        messages=[
            {"role": "system", "content": ai_role},
            {"role": "user", "content": prompt}
        ],
        model="gpt-3.5-turbo",
    ) 
    return completion.choices[0].message.content


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=('GET', 'POST'))
def contact():
    if request.method=='POST':
        print("not supported")
        flash('Thank you for your feedback')
    return render_template("contact.html")


@app.route("/service_list")
def service_list():
    return render_template("service_list.html", service_config=service_config)


@app.route('/service/<name>', methods=('GET', 'POST'))
def service(name):
    image_url = url_for('static', filename=f'images/{name}.jpg')
    current_config=service_config[name]
    guide=current_config["guide"]
    display_name=current_config["display_name"]
    current_ai_role=current_config["ai_role"]
    result = None
    if request.method == 'POST':
        prompt = request.form['title']
        result = query_open_ai(prompt, current_ai_role)

    return render_template("service.html", service_name=name, image_url=image_url, result=result, guide=guide, display_name=display_name)

if __name__ == "__main__":
    app.run(debug=True)