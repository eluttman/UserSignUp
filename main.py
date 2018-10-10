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
    return render_template('index.html')

# @app.route("/", methods=['POST']) #add locations, using POST because keeping data
# def hello():
#     username = request.form['username']
#     return render_template('WelcomePage.html',username)

# signup_form = """
# """ #i don't think I still have to do this because we used the html files vs putting html in py file


app.run()