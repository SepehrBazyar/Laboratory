from flask import Flask
from user import html_view

# config
app = Flask(__name__)

app.add_url_rule("/", 'register', html_view.register, methods=['GET', 'POST'])
app.add_url_rule("/profile/<_id>", 'profile', html_view.profile)
app.add_url_rule("/register", 'register',html_view.register, methods=['GET', 'POST'])
app.add_url_rule("/login", 'login', html_view.login, methods=['GET', 'POST'])
app.add_url_rule("/logout", 'logout', html_view.logout)
app.add_url_rule("/new_test", 'new_test', html_view.new_test)
app.add_url_rule("/test_result", 'test_result', html_view.test_result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)
