import datetime
import json
import os
import re

import psycopg2 as dbapi2

from flask import redirect
from flask import Flask
from flask import current_app
from flask import render_template, url_for
from flask.globals import session, request
from flask.templating import render_template

from flask.blueprints import Blueprint
from flask.helpers import url_for

from werkzeug import redirect
from werkzeug.debug.tbtools import render_console_html


from initialize_db import initialize_db_function




app = Flask(__name__)






def get_elephantsql_dsn(vcap_services):
    """Returns the data source name for ElephantSQL."""
    parsed = json.loads(vcap_services)
    uri = parsed["elephantsql"][0]["credentials"]["uri"]
    match = re.match('postgres://(.*?):(.*?)@(.*?)(:(\d+))?/(.*)', uri)
    user, password, host, _, port, dbname = match.groups()
    dsn = """user='{}' password='{}' host='{}' port={}
             dbname='{}'""".format(user, password, host, port, dbname)
    return dsn


@app.route('/')
@app.route('/home')
def home_page():
    now = datetime.datetime.now()
    return render_template('home.html', current_time=now.ctime())

@app.route('/initdb')
def initialize_database():
    with dbapi2.connect(app.config['dsn']) as connection:
        cursor = connection.cursor()
        initialize_db_function(cursor)
        connection.commit()
    return redirect(url_for('home_page'))

@app.route('/count')
def counter_page():
    with dbapi2.connect(app.config['dsn']) as connection:
        cursor = connection.cursor()

        query = "UPDATE COUNTER SET N = N + 1"
        cursor.execute(query)
        connection.commit()

        query = "SELECT N FROM COUNTER"
        cursor.execute(query)
        count = cursor.fetchone()[0]
    return "This page was accessed %d times." % count



@app.route('/signUp', methods=['GET', 'POST'])
def signUp():

    if request.method == 'POST':
        userName = request.form['username']
        userSurname = request.form['usersurname']
        userEmail = request.form['useremail']
        userPassword = request.form['userpassword']

        with dbapi2.connect(current_app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """INSERT INTO users (userName, userSurname, userEmail, Password) VALUES (%s, %s, %s, %s) """
            cursor.execute(query, (userName, userSurname, userEmail, userPassword))
            connection.commit()
            return redirect(url_for('profile'))

    filename ='user/signUp.html'
    return render_template(filename)


@app.route('/login')
def login():

    filename = 'user/login.html'
    return render_template(filename)

@app.route('/profile', methods=['GET','POST'])
def profile():

    filename = 'user/profile.html'

    if request.method == 'POST':
        userEmail = request.form['useremail']
        userPassword = request.form['userpassword']

        with dbapi2.connect(current_app.config['dsn']) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM users WHERE userEmail = %s AND password = %s", (userEmail, userPassword))
            connection.commit()

            result = cursor.fetchone();

            if result:
                session['role'] = result[6]
                session['id'] = result[0]
                session['name'] = result[1]
                session['surname'] = result[2]
                session['email'] = result[3]
                return render_template(filename)

    elif request.method == 'GET':
        session['role'] = ""
        session['id'] = 0
        session['name'] = ""
        session['surname'] = ""
        session['email'] = ""

        filename = 'home.html'
        return render_template(filename)

    return '<!DOCTYPE html><html><body><h1>Hatali e-posta ya da sifre</h1></body></html>'





@app.errorhandler(404)
def page_not_found(error):
    return render_template('pageNotFound.html'), 404


if __name__ == '__main__':
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    VCAP_APP_PORT = os.getenv('VCAP_APP_PORT')
    if VCAP_APP_PORT is not None:
        port, debug = int(VCAP_APP_PORT), False
    else:
        port, debug = 5000, True
    VCAP_SERVICES = os.getenv('VCAP_SERVICES')
    if VCAP_SERVICES is not None:
        app.config['dsn'] = get_elephantsql_dsn(VCAP_SERVICES)
    else:
        app.config['dsn'] = """user='postgres' password='123456'
                               host='localhost' port=5432 dbname='postgres'"""

    app.run(host='0.0.0.0', port=port, debug=debug)
