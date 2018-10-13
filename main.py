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
    password_errors = False     #wondering if we can group these in a list as "Errors" then run if errors is true return to template, else welcome
    verify_errors = False
    email_errors = False
    

    if len(username) < 3 or len(username) > 20:
        username_errors = True
    elif " " in username:
        username_errors = True
    # elif username_errors:
        # return render_template('indexExtendsBase.html', title="User signup", username_errors=username_errors, username=username)
    # else:
    #     return render_template('WelcomePage.html')
    elif len(password) < 3 or len(password) > 20:
        password_errors = True
    elif " " in password:
        password_errors = True
    elif verify_password != password:
        verify_errors = True
    # elif "@" not in email or "." not in email:
    #     email_errors = True
    # elif email == None:
    #     email_errors = False
    
#what about some sort of for loop, for error display error message? Need to get it to show all of them if they are all messed up, but not stopped by email if none input


    if username_errors:
        return render_template('indexExtendsBase.html', title="User signup", username_errors=username_errors, username=username)
    if password_errors == True:
        return render_template('indexExtendsBase.html', title="User signup", password_errors=password_errors, username=username)
    if verify_errors:
        print("This one") #NOT GETTING TO THIS ONE
        return render_template('indexExtendsBase.html', title="User signup",verify_errors=verify_errors,  username=username)
    else:
        return render_template('WelcomePage.html')


app.run()