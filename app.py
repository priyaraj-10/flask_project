# from db.db import *
from flask import Flask, render_template, url_for, request, flash, redirect, session
from flask_wtf import CSRFProtect
from flask_wtf.csrf import generate_csrf


app = Flask(__name__)

app.secret_key = 'your_secret_key'
csrf = CSRFProtect(app) 

@app.context_processor
def inject_csrf_token():
    return dict(csrf_token=generate_csrf())

@app.route("/")
def home ():
    return render_template("index.html")


@app.route("/about")
def about ():
    return render_template("about.html")


@app.route("/login", strict_slashes=False)
def loginform ():
    return render_template("login.html")

@app.route("/register", strict_slashes=False)
def registration():
    return render_template("register.html")

@app.route("/OTP", strict_slashes=False, methods=["POST"])
def OTP():
    otp=request.form
    return render_template("OTP.html")








if __name__ == "__main__":
    app.run(debug=True)