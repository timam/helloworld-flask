from flask import Flask, render_template
from flask_web_log import Log
import requests
import re

url = 'http://192.168.0.102:8080'


def gimme_data():
    data = requests.get(url)
    response = data.json()
    return response


def gimme_color():
    data = gimme_data()
    color = data['color']
    return color


def gimme_message():
    data = gimme_data()
    message = data["message"]
    return message


app = Flask(__name__)
app.config["LOG_TYPE"] = "JSON"
app.config["LOG_FILENAME"] = "helloworld-flask-log"
Log(app)


@app.route('/')
def home():
    color = gimme_color()
    message = gimme_message()
    words = re.sub("[^\w]", " ",  message).split()

    return render_template('index.html', color=color, words=words)


if __name__ == "__main__":
    app.run(debug=True)

