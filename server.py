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
from fileinput import filename




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

    filename ='signUp.html'
    return render_template(filename)


@app.route('/login')
def login():

    filename = 'login.html'
    return render_template(filename)

@app.route('/profile', methods=['GET','POST'])
def profile():



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

                filename = '{role}/profile.html'.format(role = session['role'])
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

@app.route('/userTable', methods=['GET', 'POST'])
def userTable():

    users = []
    with dbapi2.connect(current_app.config["dsn"]) as connection:
        cursor = connection.cursor()
        query = """ SELECT * FROM users;"""
        cursor.execute(query)
        for user in cursor:
            users.append(user)
        connection.commit()


    if request.method == 'POST':
        userName = request.form['userName']
        userSurname = request.form['userSurname']
        userEmail = request.form['userEmail']
        userPassword = request.form['userPassword']
        userBalance = request.form['userBalance']
        userRole = request.form['userRole']

        with dbapi2.connect(current_app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """INSERT INTO users (userName, userSurname, userEmail, Password, userBalance, role) VALUES (%s, %s, %s, %s, %s, %s) """
            cursor.execute(query, (userName, userSurname, userEmail, userPassword, userBalance, userRole))
            connection.commit()
            return redirect(url_for('userTable'))

    filename = 'admin/user.html'
    return render_template(filename, users=users)



@app.route('/userTable/deletedItem/<int:id>', methods=['GET', 'POST'])
def userTableDelete(id):
    with dbapi2.connect(current_app.config["dsn"]) as connection:
        cursor = connection.cursor()
        cursor.execute(" DELETE  FROM users WHERE id = %s ", [id])
        connection.commit()

    return redirect(url_for('userTable'))

@app.route('/userTableUpdate', methods=['GET', 'POST'])
def userTableUpdate():
    filename = 'admin/userUpdate.html'
    return render_template(filename)






@app.route('/matchTable', methods=['GET', 'POST'])
def matchTable():

    matches = []
    with dbapi2.connect(current_app.config["dsn"]) as connection:
        cursor = connection.cursor()
        query = """ SELECT * FROM match;"""
        cursor.execute(query)
        for match in cursor:
            matches.append(match)
        connection.commit()


    if request.method == 'POST':
        matchTime = request.form['matchTime']
        matchDate = request.form['matchDate']
        homeTeamId = request.form['homeTeamId']
        homeTeamScore = request.form['homeTeamScore']
        guestTeam = request.form['guestTeam']
        guestTamScore = request.form['guestTamScore']
        result = request.form['result']

        with dbapi2.connect(current_app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """INSERT INTO match (matchTime, matchDate, homeTeamId, homeTeamScore, guestTeam, guestTamScore, result) VALUES (%s, %s, %s, %s, %s, %s, %s) """
            cursor.execute(query, (matchTime, matchDate, homeTeamId, homeTeamScore, guestTeam, guestTamScore, result))
            connection.commit()
            return redirect(url_for('matchTable'))

    filename = 'admin/match.html'
    return render_template(filename, matches=matches)

@app.route('/matchTable/deletedItem/<int:id>', methods=['GET', 'POST'])
def matchTableDelete(id):
    with dbapi2.connect(current_app.config["dsn"]) as connection:
        cursor = connection.cursor()
        cursor.execute(" DELETE  FROM match WHERE id = %s ", [id])
        connection.commit()

    return redirect(url_for('matchTable'))

@app.route('/matchTableUpdate', methods=['GET', 'POST'])
def matchTableUpdate():
    filename = 'admin/matchUpdate.html'
    return render_template(filename)

@app.route('/teamTable', methods=['GET', 'POST'])
def teamTable():

    teams = []
    with dbapi2.connect(current_app.config["dsn"]) as connection:
        cursor = connection.cursor()
        query = """ SELECT * FROM teams;"""
        cursor.execute(query)
        for team in cursor:
            teams.append(team)
        connection.commit()


    if request.method == 'POST':
        teamName = request.form['teamName']
        teamLeague = request.form['teamLeague']
        teamChampionsLeague = request.form['teamChampionsLeague']
        teamUefaLeague = request.form['teamUefaLeague']
        teamCountry = request.form['teamCountry']

        with dbapi2.connect(current_app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """INSERT INTO teams (teamName, teamLeague, teamChampionsLeague, teamUefaLeague, teamCountry) VALUES (%s, %s, %s, %s, %s) """
            cursor.execute(query, (teamName, teamLeague, teamChampionsLeague, teamUefaLeague, teamCountry))
            connection.commit()
            return redirect(url_for('teamTable'))

    filename = 'admin/team.html'
    return render_template(filename, teams=teams)

@app.route('/teamTable/deletedItem/<int:id>', methods=['GET', 'POST'])
def teamTableDelete(id):
    with dbapi2.connect(current_app.config["dsn"]) as connection:
        cursor = connection.cursor()
        cursor.execute(" DELETE  FROM teams WHERE id = %s ", [id])
        connection.commit()

    return redirect(url_for('teamTable'))

@app.route('/teamTableUpdate', methods=['GET', 'POST'])
def teamTableUpdate():
    filename = 'admin/teamUpdate.html'
    return render_template(filename)

@app.route('/leagueTable', methods=['GET', 'POST'])
def leagueTable():

    leagues = []
    with dbapi2.connect(current_app.config["dsn"]) as connection:
        cursor = connection.cursor()
        query = """ SELECT * FROM leagues;"""
        cursor.execute(query)
        for league in cursor:
            leagues.append(league)
        connection.commit()


    if request.method == 'POST':
        leagueName = request.form['leagueName']
        country = request.form['country']


        with dbapi2.connect(current_app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """INSERT INTO leagues (leagueName, country) VALUES (%s, %s) """
            cursor.execute(query, (leagueName, country))
            connection.commit()
            return redirect(url_for('leagueTable'))

    filename = 'admin/league.html'
    return render_template(filename, leagues=leagues)

@app.route('/leagueTable/deletedItem/<int:id>', methods=['GET', 'POST'])
def leagueTableDelete(id):
    with dbapi2.connect(current_app.config["dsn"]) as connection:
        cursor = connection.cursor()
        cursor.execute(" DELETE  FROM leagues WHERE id = %s ", [id])
        connection.commit()

    return redirect(url_for('leagueTable'))

@app.route('/leagueTableUpdate', methods=['GET', 'POST'])
def leagueTableUpdate():
    filename = 'admin/league_update.html'
    return render_template(filename)

@app.route('/leaguePositionTable', methods=['GET', 'POST'])
def leaguePositionTable():

    leaguePositions = []
    with dbapi2.connect(current_app.config["dsn"]) as connection:
        cursor = connection.cursor()
        query = """ SELECT * FROM leaguePosition;"""
        cursor.execute(query)
        for leaguePositio in cursor:
            leaguePositions.append(leaguePositio)
        connection.commit()


    if request.method == 'POST':
        leagueName = request.form['leagueName']
        teamName = request.form['teamName']
        oynanan = request.form['oynanan']
        galibiyet = request.form['galibiyet']
        beraberlik = request.form['beraberlik']
        yenilgi = request.form['yenilgi']
        atilanGol = request.form['atilanGol']
        yenilenGol = request.form['yenilenGol']
        puan = request.form['puan']
        country = request.form['country']


        with dbapi2.connect(current_app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """INSERT INTO leaguePosition (leagueName, teamName, oynanan, galibiyet, beraberlik, yenilgi, atilanGol, yenilenGol, puan, country) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """
            cursor.execute(query, (leagueName, teamName, oynanan, galibiyet, beraberlik, yenilgi, atilanGol, yenilenGol, puan, country))
            connection.commit()
            return redirect(url_for('leaguePositionTable'))

    filename = 'admin/league_position.html'
    return render_template(filename, leaguePositions=leaguePositions)

@app.route('/leaguePositionTable/deletedItem/<int:id>', methods=['GET', 'POST'])
def leaguePositionTableDelete(id):
    with dbapi2.connect(current_app.config["dsn"]) as connection:
        cursor = connection.cursor()
        cursor.execute(" DELETE  FROM leagueposition WHERE id = %s ", [id])
        connection.commit()

    return redirect(url_for('leaguePositionTable'))

@app.route('/leaguePositionTableUpdate', methods=['GET', 'POST'])
def leaguePositionTableUpdate():
    filename = 'admin/league_position_update.html'
    return render_template(filename)

@app.route('/wagerTable', methods=['GET', 'POST'])
def wagerTable():

    wagers = []
    with dbapi2.connect(current_app.config["dsn"]) as connection:
        cursor = connection.cursor()
        query = """ SELECT * FROM wager;"""
        cursor.execute(query)
        for w in cursor:
            wagers.append(w)
        connection.commit()


    if request.method == 'POST':
        matchId = request.form['matchId']
        userExpect = request.form['userExpect']
        wagerValue = request.form['wagerValue']
        wagerWin = request.form['wagerWin']
        userId = request.form['userId']


        with dbapi2.connect(current_app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """INSERT INTO wager (matchId, userExpect, wagerValue, wagerWin, userId) VALUES (%s, %s, %s, %s, %s) """
            cursor.execute(query, (matchId, userExpect, wagerValue, wagerWin, userId))
            connection.commit()
            return redirect(url_for('wagerTable'))

    filename = 'admin/wager.html'
    return render_template(filename, wagers=wagers)

@app.route('/wagerTable/deletedItem/<int:id>', methods=['GET', 'POST'])
def wagerTableDelete(id):
    with dbapi2.connect(current_app.config["dsn"]) as connection:
        cursor = connection.cursor()
        cursor.execute(" DELETE  FROM wager WHERE id = %s ", [id])
        connection.commit()

    return redirect(url_for('wagerTable'))

@app.route('/wagerTableUpdate', methods=['GET', 'POST'])
def wagerTableUpdate():
    filename = 'admin/wager_update.html'
    return render_template(filename)










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
