#!/usr/bin/env python3
"""use_of_templates/app.py
Develop the power of Flask and Jinja by creating HTML templates,
expending those templates, and pass variable to create dynamic content.
"""

import datetime  # import a library to manage dates

from flask import request

import flask # import the flask library


app = flask.Flask(__name__)  # instantiate a minimal webserver


@app.route('/')  # create the index route
def index():
    # we moved the HTML inside the 'templates/' directory
    # the documentation for the template engine is available here:
    # https://jinja.palletsprojects.com/

    return flask.render_template('index.html')


@app.route('/time/')  # create a new route
def time():
    now = datetime.datetime.now()
    date = now.strftime('%d/%m/%Y')
    hour = now.strftime('%H:%M')

    # we can pass some data to the template to create dynamic content
    # to create variables inside the template, use keywords arguments with
    # name=value
    return flask.render_template('time.html', date=date, hour=hour)
    
# creating a new route for the form
@app.route('/form/', methods=['POST', 'GET'])
def form():
    return flask.render_template('form.html')


# creating a new route for showing advices and name of the writter
@app.route('/advice/', methods=['POST'])
def advice():
    lastname = request.form['lastname']
    firstname = request.form['firstname']
    advice = request.form['advice']
    return flask.render_template('advice.html', lastname=lastname, firstname=firstname, advice=advice)


if __name__ == '__main__':  # consider this line as the main
    app.run('0.0.0.0', 8080, debug=True)  # start web server in debug mode on port 8080
