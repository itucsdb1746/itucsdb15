Ekleme
^^^^^^

Veritabanına ekleme operasyonları "server.py" da bulunur.

Kullanıcı ekleme:
Değerleri ekleme yetkisine sahip kullanıcıdan alır.::
   .. code-block:: python
      if request.method == 'POST':
        userName = request.form['userName']
        userSurname = request.form['userSurname']
        userEmail = request.form['userEmail']
        userPassword = request.form['userPassword']
        userBalance = request.form['userBalance']
        userRole = request.form['userRole']

Bu değerleri aşağıdaki yapı ile veritabanına işler.::
      .. code-block:: python
         with dbapi2.connect(current_app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """INSERT INTO users (userName, userSurname, userEmail, Password, userBalance, role) VALUES (%s, %s, %s, %s, %s, %s) """
            cursor.execute(query, (userName, userSurname, userEmail, userPassword, userBalance, userRole))
            connection.commit()
            return redirect(url_for('userTable'))

Kullanıcı ekleme operasyonu bitmiş olur.

Maç ekleme:
Değerleri ekleme yetkisine sahip kullanıcıdan alır.::
   .. code-block:: python
      if request.method == 'POST':
        matchTime = request.form['matchTime']
        matchDate = request.form['matchDate']
        homeTeamId = request.form['homeTeamId']
        homeTeamScore = request.form['homeTeamScore']
        guestTeam = request.form['guestTeam']
        guestTamScore = request.form['guestTamScore']
        result = request.form['result']

Bu değerleri aşağıdaki yapı ile veritabanına işler.::
      .. code-block:: python
         with dbapi2.connect(current_app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """INSERT INTO match (matchTime, matchDate, homeTeamId, homeTeamScore, guestTeam, guestTamScore, result) VALUES (%s, %s, %s, %s, %s, %s, %s) """
            cursor.execute(query, (matchTime, matchDate, homeTeamId, homeTeamScore, guestTeam, guestTamScore, result))
            connection.commit()
            return redirect(url_for('matchTable'))

Maç ekleme operasyonu bitmiş olur.

Takım ekleme:
Değerleri ekleme yetkisine sahip kullanıcıdan alır.::
   .. code-block:: python
      if request.method == 'POST':
        teamName = request.form['teamName']
        teamLeague = request.form['teamLeague']
        teamChampionsLeague = request.form['teamChampionsLeague']
        teamUefaLeague = request.form['teamUefaLeague']
        teamCountry = request.form['teamCountry']

Bu değerleri aşağıdaki yapı ile veritabanına işler.::
      .. code-block:: python
         with dbapi2.connect(current_app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """INSERT INTO teams (teamName, teamLeague, teamChampionsLeague, teamUefaLeague, teamCountry) VALUES (%s, %s, %s, %s, %s) """
            cursor.execute(query, (teamName, teamLeague, teamChampionsLeague, teamUefaLeague, teamCountry))
            connection.commit()
            return redirect(url_for('teamTable'))

Takım ekleme operasyonu bitmiş olur.

Lig ekleme:
Değerleri ekleme yetkisine sahip kullanıcıdan alır.::
   .. code-block:: python
      if request.method == 'POST':
        leagueName = request.form['leagueName']
        country = request.form['country']

Bu değerleri aşağıdaki yapı ile veritabanına işler.::
      .. code-block:: python
         with dbapi2.connect(current_app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """INSERT INTO leagues (leagueName, country) VALUES (%s, %s) """
            cursor.execute(query, (leagueName, country))
            connection.commit()
            return redirect(url_for('leagueTable'))

Lig ekleme operasyonu bitmiş olur.

Lig Durumu ekleme:
Değerleri ekleme yetkisine sahip kullanıcıdan alır.::
   .. code-block:: python
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

Bu değerleri aşağıdaki yapı ile veritabanına işler.::
      .. code-block:: python
         with dbapi2.connect(current_app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """INSERT INTO leaguePosition (leagueName, teamName, oynanan, galibiyet, beraberlik, yenilgi, atilanGol, yenilenGol, puan, country) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """
            cursor.execute(query, (leagueName, teamName, oynanan, galibiyet, beraberlik, yenilgi, atilanGol, yenilenGol, puan, country))
            connection.commit()
            return redirect(url_for('leaguePositionTable'))

Lig Durumu ekleme operasyonu bitmiş olur.

Bahis ekleme:
Değerleri ekleme yetkisine sahip kullanıcıdan alır.::
   .. code-block:: python
      if request.method == 'POST':
        matchId = request.form['matchId']
        userExpect = request.form['userExpect']
        wagerValue = request.form['wagerValue']
        wagerWin = request.form['wagerWin']
        userId = request.form['userId']

Bu değerleri aşağıdaki yapı ile veritabanına işler.::
      .. code-block:: python
         with dbapi2.connect(current_app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """INSERT INTO wager (matchId, userExpect, wagerValue, wagerWin, userId) VALUES (%s, %s, %s, %s, %s) """
            cursor.execute(query, (matchId, userExpect, wagerValue, wagerWin, userId))
            connection.commit()
            return redirect(url_for('wagerTable'))

Bahis ekleme operasyonu bitmiş olur.

Silme
^^^^^
Veritabanından silme operasyonları "server.py" da bulunur ve id değerlerini htmldeki request içinde gönderiyoruz.
Kullanıcı silme:::
      .. code-block:: python
         with dbapi2.connect(current_app.config["dsn"]) as connection:
            cursor = connection.cursor()
            cursor.execute(" DELETE  FROM users WHERE id = %s ", [id])
            connection.commit()

Kullanıcı silme tamamlanmıştır.

Maç silme:::
      .. code-block:: python
         with dbapi2.connect(current_app.config["dsn"]) as connection:
            cursor = connection.cursor()
            cursor.execute(" DELETE  FROM match WHERE id = %s ", [id])
            connection.commit()

Maç silme tamamlanmıştır.


Takım silme:::
      .. code-block:: python
         with dbapi2.connect(current_app.config["dsn"]) as connection:
            cursor = connection.cursor()
            cursor.execute(" DELETE  FROM teams WHERE id = %s ", [id])
            connection.commit()

Takım silme tamamlanmıştır.


Lig silme:::
      .. code-block:: python
         with dbapi2.connect(current_app.config["dsn"]) as connection:
            cursor = connection.cursor()
            cursor.execute(" DELETE  FROM leagues WHERE id = %s ", [id])
            connection.commit()

Lig silme tamamlanmıştır.

Lig Durumu silme:::
      .. code-block:: python
         with dbapi2.connect(current_app.config["dsn"]) as connection:
            cursor = connection.cursor()
            cursor.execute(" DELETE  FROM leagueposition WHERE id = %s ", [id])
            connection.commit()

Lig Durumu silme tamamlanmıştır.


Bahis silme:::
      .. code-block:: python
         with dbapi2.connect(current_app.config["dsn"]) as connection:
            cursor = connection.cursor()
            cursor.execute(" DELETE  FROM wager WHERE id = %s ", [id])
            connection.commit()

Bahis silme tamamlanmıştır.

Güncelleme
^^^^^^^^^^

Veritabanında güncelleme operasyonları "server.py" da bulunur ve id değerlerini htmldeki request içinde gönderiyoruz.
Kullanıcı güncelleme:
Değerleri güncelleme yetkisine sahip kullanıcıdan alır.::
   .. code-block:: python
      if request.method =='POST':
        userName = request.form['userName']
        userSurname = request.form['userSurname']
        userEmail = request.form['userEmail']
        password = request.form['password']
        userBalance = request.form['userBalance']
        role = request.form['role']

Bu değerleri aşağıdaki yapı ile veritabanına işler.::
      .. code-block:: python
         with dbapi2.connect(current_app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """ UPDATE users  SET userName=%s, userSurname=%s, userEmail=%s, password=%s, userBalance=%s, role=%s WHERE (id =%s)"""
            cursor.execute(query, (userName, userSurname, userEmail, password, userBalance, role, id))
            connection.commit()
            return redirect(url_for('userTable'))

Maç güncelleme:
Değerleri güncelleme yetkisine sahip kullanıcıdan alır.::
   .. code-block:: python
      if request.method =='POST':
        matchTime = request.form['matchTime']
        matchDate = request.form['matchDate']
        hometeamid = request.form['hometeamid']
        hometeamScore = request.form['hometeamScore']
        guestteam = request.form['guestteam']
        guesttamscore = request.form['guesttamscore']
        result = request.form['result']

Bu değerleri aşağıdaki yapı ile veritabanına işler.::
      .. code-block:: python
         with dbapi2.connect(current_app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """ UPDATE match  SET matchTime=%s, matchDate=%s, hometeamid=%s, hometeamScore=%s, guestteam=%s, guesttamscore=%s, result=%s WHERE (id =%s)"""
            cursor.execute(query, (matchTime, matchDate, hometeamid, hometeamScore, guestteam, guesttamscore, result, id))
            connection.commit()
            return redirect(url_for('matchTable'))

Takım güncelleme:
Değerleri güncelleme yetkisine sahip kullanıcıdan alır.::
   .. code-block:: python
      if request.method =='POST':
        teamName = request.form['teamName']
        teamleague = request.form['teamleague']
        teamchampionsleague = request.form['teamchampionsleague']
        teamuefaleague = request.form['teamuefaleague']
        teamcountry = request.form['teamcountry']

Bu değerleri aşağıdaki yapı ile veritabanına işler.::
      .. code-block:: python
         with dbapi2.connect(current_app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """ UPDATE teams  SET teamName=%s, teamleague=%s, teamchampionsleague=%s, teamuefaleague=%s, teamcountry=%s WHERE (id =%s)"""
            cursor.execute(query, (teamName, teamleague, teamchampionsleague, teamuefaleague, teamcountry, id))
            connection.commit()
            return redirect(url_for('teamTable'))

Lig güncelleme:
Değerleri güncelleme yetkisine sahip kullanıcıdan alır.::
   .. code-block:: python
      if request.method =='POST':
        leagueName = request.form['leagueName']
        country = request.form['country']

Bu değerleri aşağıdaki yapı ile veritabanına işler.::
      .. code-block:: python
         with dbapi2.connect(current_app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """ UPDATE leagues  SET leagueName=%s, country=%s WHERE (id =%s)"""
            cursor.execute(query, (leagueName, country, id))
            connection.commit()
            return redirect(url_for('leagueTable'))

Lig Durumu güncelleme:
Değerleri güncelleme yetkisine sahip kullanıcıdan alır.::
   .. code-block:: python
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

Bu değerleri aşağıdaki yapı ile veritabanına işler.::
      .. code-block:: python
         with dbapi2.connect(current_app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """INSERT INTO leaguePosition (leagueName, teamName, oynanan, galibiyet, beraberlik, yenilgi, atilanGol, yenilenGol, puan, country) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """
            cursor.execute(query, (leagueName, teamName, oynanan, galibiyet, beraberlik, yenilgi, atilanGol, yenilenGol, puan, country))
            connection.commit()
            return redirect(url_for('leaguePositionTable'))

Bahis güncelleme:
Değerleri güncelleme yetkisine sahip kullanıcıdan alır.::
   .. code-block:: python
      if request.method =='POST':
        matchId = request.form['matchId']
        userExpect = request.form['userExpect']
        wagerValue = request.form['wagerValue']
        wagerWin = request.form['wagerWin']
        userId = request.form['userId']

Bu değerleri aşağıdaki yapı ile veritabanına işler.::
      .. code-block:: python
         with dbapi2.connect(current_app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """ UPDATE wager  SET matchId=%s,userExpect=%s, wagerValue=%s, wagerWin=%s, userId=%s WHERE (id =%s)"""
            cursor.execute(query, (matchId,userExpect, wagerValue, wagerWin, userId, id))
            connection.commit()
            return redirect(url_for('wagerTable'))
