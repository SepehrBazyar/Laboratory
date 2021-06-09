from flask import Flask, render_template, request, redirect
from .models import *


def profile(_id):
    user = Patient.patients[int(_id)]
    return render_template("resume.html", data=user)


def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        _vars = request.form
        Patient(_vars.get("username").split(" ", 1)[0],
                _vars.get("username").split(" ", 1)[1],
                _vars.get("national"),
                _vars.get("phone"),
                _vars.get("email"),
                password=_vars.get("password"),)

    return redirect(f"/profile/{len(Patient.patients)-1}")


def login():
    if request.method == "GET":
        pass
    else:
        pass
