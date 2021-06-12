from flask import Flask, render_template, request, redirect
from .models import *


def profile(_id):
    user = Patient.patients[_id]
    return render_template("resume.html", data=user)


def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        _vars = request.form
        Patient(_vars.get("username").split(" ", 1)[0],
                _vars.get("username").split(" ", 1)[1],
                _vars.get("national"), _vars.get("phone"),
                _vars.get("password"), "male", 20,
                "O", _vars.get("email"))

    return redirect(f"/profile/{'1' + _vars.get('national')}")


def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        _vars = request.form
        user = Patient._FILE.read('1' + _vars.get('national'))
        if user and user['password'] == sha256(_vars.get('password').encode()).hexdigest():
            print(_vars.get('remember'))
            return redirect(f"/profile/{'1' + _vars.get('national')}")
        return render_template("login.html")
