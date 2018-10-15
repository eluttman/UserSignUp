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
    verified_password = request.form['verify']
    email = request.form['email']

    email_errors = False


#USERNAME CHECK
    username_errors = determine_username_errors(username)

#PASSWORD CHECK
    password_errors = determine_password_errors(password)

#VERIFICATION OF PASSWORD CHECK
    verification_errors_exist = determine_verification_errors_exist(verified_password, password)
    
#VALID EMAIL CHECK
    email_errors = determine_email_errors(email)
    

# Error Check if no Errors redirect to Welcome Page
    if username_errors or password_errors or verification_errors_exist or email_errors:
        return render_template('indexExtendsBase.html', title="User signup",username=username, username_errors=username_errors, password_errors=password_errors, verification_errors_exist=verification_errors_exist, email=email, email_errors=email_errors)
    else:
        return render_template('WelcomePage.html', username=username)

def determine_username_errors(username):
        if len(username) < 3 or len(username) > 20:
            return True
        elif " " in username:
            return True
        else:
            return False
def determine_password_errors(password):
        if len(password) < 3 or len(password) > 20:
            return True
        elif " " in password:
            return True
        else:
            return False
def determine_verification_errors_exist(verified_password, password):
        if verified_password != password:
            return True
        elif verified_password == '':
            return True
        else:
            return False

def determine_email_errors(email):
        if email == "":
            return False
        elif "@" not in email or "." not in email:
            return  True



app.run()