import re
from datetime import datetime

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, Flask!"


@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/parseResume/")
@app.route("/parseResume/<fileUrl>")
def hello_there(fileUrl = None):
    return render_template(
        "hello_there.html",
        fileUrl=fileUrl,
        date=datetime.now()
    )