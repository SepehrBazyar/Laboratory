from datetime import timedelta
from flask import render_template, request, redirect, make_response
from flask.helpers import url_for

from core.utility import retrieve_user
from .models import *
from core.manager import *

db_manger = DatabaseManager()

def profile(_id):
    cookies = request.cookies
    if cookies.get('_ID'):
        check_res = db_manger.check_record('users', national_code=_id)
        user = retrieve_user(check_res[0])
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
                user_type = _vars.get("user_type")
                user_type_id = db_manger.get_id('user_type', type=user_type)
                # extra_data = (db_manger.read('user_type', row_id=user_type_id))[0][1]
                # extra_data = json.dumps(extra_data)
                # extra_data_dict = json.loads(extra_data)
                # for key, value in extra_data_dict.items():
                #     value = input(f"enter your {key}:")
                #     extra_data_dict.update({f"{key}": f"{value}"})
                first_name = _vars.get("username").split(" ", 1)[0]
                last_name = _vars.get("username").split(" ", 1)[1]
                national_code = _vars.get("national")
                phone = _vars.get("phone")
                password = _vars.get("password")
                email = _vars.get("email")
                if user_type == 'patient':
                    extra_data_dict = {"gender":_vars.get("gender"), "age":_vars.get("age"), "blood_type":_vars.get("blood_type")}
                    user = Patient(first_name=first_name, last_name=last_name, national_code=national_code,
                                          phone=phone,
                                          password=password, email=email, **extra_data_dict)
                elif user_type == 'doctor':
                    extra_data_dict = {"expertise": _vars.get("expertise")}
                    user = Doctor(first_name=first_name, last_name=last_name, national_code=national_code,
                                         phone=phone,
                                         password=password, email=email, **extra_data_dict)
                elif user_type == 'operator':
                    extra_data_dict = {"licence": _vars.get("licence")}
                    user = Operator(first_name=first_name, last_name=last_name, national_code=national_code,
                                           phone=phone,
                                           password=password, email=email, **extra_data_dict)
                db_manger.create(table="users", model=user)
                print("Congrats. Your Account Is Created")
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
            # user = Patient._FILE.read('1' + _vars.get('national'))
            password_hashed = sha256(_vars.get('password').encode()).hexdigest()
            check_res = db_manger.check_record('users', national_code=_vars.get('national'), password=password_hashed)
            if check_res:
                user = retrieve_user(check_res[0])
                if user and user.password == password_hashed:
                    html_str = redirect(f"/profile/{'1' + _vars.get('national')}")
                    resp = make_response(html_str)
                    if _vars.get('remember'):
                        resp.set_cookie(
                            '_ID', '1' + _vars.get('national'), max_age=timedelta(weeks=1))
                    else:
                        resp.set_cookie('_ID', '1' + _vars.get('national'))
                    return resp
            return render_template("login.html")


def logout():
    resp = redirect("/login")
    resp.delete_cookie('_ID')
    return resp
