from flask import Flask, render_template, request
from user import html_view

# config
app = Flask(__name__)

app.add_url_rule("/profile/<_id>", 'profile', html_view.profile)
app.add_url_rule("/register", 'register',
                 html_view.register, methods=['GET', 'POST'])
app.add_url_rule("/login", 'login', html_view.login, methods=['GET', 'POST'])

app.run(port=8001)
