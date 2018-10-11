from flask import Flask, request, redirect, render_template
import cgi
import os
#where do i put the autoescape if not using jinja

app = Flask(__name__)
app.config['DEBUG'] = True



# @app.route("/") #add locations
# def display_signup_form():
#     return signup_form.format(#username='', username_error='',
#     #password='', password_error='', email='', email_error='')

@app.route("/")#add locations
def index():
    title = "User signup"
    return render_template('indexExtendsBase.html', title=title)

@app.route("/", methods=['POST']) #add locations, using POST because keeping data
def hello():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify']
    email = request.form['email']

    username_errors = False

    if len(username) < 3 or len(username) > 20:
        username_errors = True
    elif " " in username:
        username_errors = True

    
    if username_errors:
        return render_template('indexExtendsBase.html', title="User signup", username_errors=username_errors, username=username)
    else:
        return render_template('WelcomePage.html')

# signup_form = """
# """ #i don't think I still have to do this because we used the html files vs putting html in py file


app.run()