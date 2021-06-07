from flask import Flask, render_template, request
from user import html_view

# config
app = Flask(__name__)

app.add_url_rule("/profile", 'profile', html_view.profile)

app.run(port=8001)
