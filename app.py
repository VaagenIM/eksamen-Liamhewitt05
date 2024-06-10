from flask import Flask, render_template, request, url_for
from dotenv import load_dotenv
import os
from openai import OpenAI
from service_config import service_config
load_dotenv()

app = Flask(__name__)

OPENAI_KEY = os.environ.get("OPENAI_KEY")
open_ai_client = OpenAI(
    api_key=OPENAI_KEY
)

def query_open_ai(prompt, ai_role, outputs=3): 
    completion = open_ai_client.chat.completions.create(
        messages=[
            {"role": "system", "content": ai_role},
            {"role": "user", "content": prompt}
        ],
        model="gpt-3.5-turbo",
    ) 
    print(completion.choices[0].message.content)
    # output = list() 
    # for k in response['choices']: 
    #     output.append(k['text'].strip()) 
    return completion.choices[0].message.content

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


@app.route('/service/<name>', methods=('GET', 'POST'))
def service(name):
    image_url = url_for('static', filename=f'images/{name}.jpg')
    current_config=service_config[name]
    current_ai_role=current_config["ai_role"]
    result = None
    if request.method == 'POST':
        prompt = request.form['title']
        result = query_open_ai(prompt, current_ai_role)

    return render_template("service.html", service_name=name, image_url=image_url, result=result)

if __name__ == "__main__":
    app.run(debug=True)