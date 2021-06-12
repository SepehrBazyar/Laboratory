from datetime import timedelta
from flask import render_template, request, redirect, make_response
from flask.helpers import url_for
from .models import *


def profile(_id):
    cookies = request.cookies
    if cookies.get('_ID'):
        user = Patient.patients[_id]
        return render_template("resume.html", data=user)
    else:
        return redirect(url_for('register'))


def register():
    cookies = request.cookies
    if cookies.get('_ID'):
        return redirect(f"/profile/{cookies.get('_ID')}")
    else:
        if request.method == "GET":
            return render_template("register.html")
        else:
            _vars = request.form
            try:
                Patient(_vars.get("username").split(" ", 1)[0],
                        _vars.get("username").split(" ", 1)[1],
                        _vars.get("national"), _vars.get("phone"),
                        _vars.get("password"), "male", 20,
                        "O", _vars.get("email") or None)
            except AssertionError:
                return render_template("register.html")
            else:
                html_str = redirect(f"/profile/{'1' + _vars.get('national')}")
                resp = make_response(html_str)
                resp.set_cookie('_ID', '1' + _vars.get('national'))
                return resp


def login():
    cookies = request.cookies
    if cookies.get('_ID'):
        return redirect(f"/profile/{cookies.get('_ID')}")
    else:
        if request.method == "GET":
            return render_template("login.html")
        else:
            _vars = request.form
            user = Patient._FILE.read('1' + _vars.get('national'))
            if user and user['password'] == sha256(_vars.get('password').encode()).hexdigest():
                html_str = redirect(f"/profile/{'1' + _vars.get('national')}")
                resp = make_response(html_str)
                if _vars.get('remember'):
                    resp.set_cookie('_ID', '1' + _vars.get('national'), max_age=timedelta(weeks=1))
                else:
                    resp.set_cookie('_ID', '1' + _vars.get('national'))
                return resp
            return render_template("login.html")
