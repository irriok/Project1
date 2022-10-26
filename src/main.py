import sys, os
sys.path.append(".")
from src.app import views
from flask import Flask, redirect, url_for, render_template, request


app = Flask(__name__)

@app.route("/post", methods=["GET"])
def post():
    # if request.method == "POST":
    new_request = views.APIView()
    new_request.post()


if __name__ == "__main__":
    app.run(debug=True)

