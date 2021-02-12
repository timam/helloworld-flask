import string

from flask import Flask, render_template
import requests

url = 'http://localhost:8080'


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


@app.route('/')
def home():
    color = gimme_color()
    message = gimme_message()
    return render_template('index.html', color=color, message=message)


if __name__ == "__main__":
    app.run()
