from flask import Flask, render_template
from .models import *

user = Patient("DR H", ".Rouhani", "5120000045", "09152225555", "h.rouani@fesad.ir", password="h.rouahni")


def profile():
    return render_template("resume.html", data=user)
