import os
from flask import flask, render_template

app = (__name__)

@app.route("/")
def index():
    return render_template("index.html")