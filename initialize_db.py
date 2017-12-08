def initialize_db_function(cursor):

#counter table definition
    cursor.execute("""DROP TABLE IF EXISTS COUNTER""")
    cursor.execute("""CREATE TABLE COUNTER (N INTEGER)""")
    cursor.execute("""INSERT INTO COUNTER (N) VALUES (0)""")

#users table definition
    cursor.execute("""DROP TABLE IF EXISTS users CASCADE""")
    cursor.execute("""CREATE TABLE users(
                        id SERIAL PRIMARY KEY NOT NULL,
                        userName VARCHAR(30),
                        userSurname VARCHAR(30),
                        userEmail VARCHAR(50) UNIQUE,
                        password VARCHAR(30),
                        userBalance INTEGER DEFAULT '0',
                        role VARCHAR(10) DEFAULT 'user')""")

#users table inserting data
    cursor.execute("""INSERT INTO users (userName, userSurname, userEmail, password, userBalance, role)
                                    VALUES('samet', 'bulut', 'samet_bulut_101@hotmail.com', 'qwerty', '200', 'admin')""")
    cursor.execute("""INSERT INTO users (userName, userSurname, userEmail, password, userBalance, role)
                                    VALUES('mehmet', 'yılmaz', 'yilmazmehmet@hotmail.com', '123456', '150', 'admin')""")
    cursor.execute("""INSERT INTO users (userName, userSurname, userEmail, password, userBalance, role)
                                    VALUES('ahmet', 'yılmaz', 'yilmazahmet@hotmail.com', '123456', '350', 'admin')""")
    cursor.execute("""INSERT INTO users (userName, userSurname, userEmail, password, userBalance, role)
                                    VALUES('ezgi', 'yılmaz', 'yilmazezgi@hotmail.com', 'qwerty', '450', 'admin')""")
    cursor.execute("""INSERT INTO users (userName, userSurname, userEmail, password, userBalance, role)
                                    VALUES('admin', 'yılmaz', 'admin@test.com', 'qwerty', '600', 'admin')""")
    cursor.execute("""INSERT INTO users (userName, userSurname, userEmail, password, userBalance, role)
                                    VALUES('test', 'yılmaz', 'test@test.com', 'qwerty', '600', 'user')""")

#leagues table definition
    cursor.execute("""DROP TABLE IF EXISTS leagues CASCADE""")
    cursor.execute("""CREATE TABLE leagues(
                        id SERIAL PRIMARY KEY NOT NULL,
                        leagueName VARCHAR(30),
                        country VARCHAR(30))""")

#leagues table inserting data
    cursor.execute("""INSERT INTO leagues (leagueName, country)
                                        VALUES('La Liga', 'ispanya')""")
    cursor.execute("""INSERT INTO leagues (leagueName, country)
                                        VALUES('İngiltere Premier ligi', 'ingiltere')""")
    cursor.execute("""INSERT INTO leagues (leagueName, country)
                                        VALUES('Spor Toto Super lig', 'türkiye')""")
    cursor.execute("""INSERT INTO leagues (leagueName, country)
                                        VALUES('Bundesliga', 'almanya')""")
    cursor.execute("""INSERT INTO leagues (leagueName, country)
                                        VALUES('Ligue 1', 'fransa')""")

#teams table definition
    cursor.execute("""DROP TABLE IF EXISTS teams CASCADE""")
    cursor.execute("""CREATE TABLE teams(
                        id SERIAL PRIMARY KEY NOT NULL,
                        teamName VARCHAR(30),
                        teamLeague integer references leagues(id) ON DELETE RESTRICT ON UPDATE CASCADE,
                        teamChampionsLeague BOOLEAN,
                        teamUefaLeague BOOLEAN,
                        teamCountry integer references leagues(id) ON DELETE RESTRICT ON UPDATE CASCADE)""")

#teams table inserting data
    cursor.execute("""INSERT INTO teams (teamName, teamLeague, teamChampionsLeague, teamUefaLeague, teamCountry)
                                    VALUES('Real Madrid', '1', true, false, '1')""")
    cursor.execute("""INSERT INTO teams (teamName, teamLeague, teamChampionsLeague, teamUefaLeague, teamCountry)
                                    VALUES('Barcelona', '1', true, false, '1')""")
    cursor.execute("""INSERT INTO teams (teamName, teamLeague, teamChampionsLeague, teamUefaLeague, teamCountry)
                                    VALUES('Atletico Madrid', '1', true, false, '1')""")
    cursor.execute("""INSERT INTO teams (teamName, teamLeague, teamChampionsLeague, teamUefaLeague, teamCountry)
                                    VALUES('Valencia', '1', false, true, '1')""")
    cursor.execute("""INSERT INTO teams (teamName, teamLeague, teamChampionsLeague, teamUefaLeague, teamCountry)
                                    VALUES('Sevilla', '1', false, true, '1')""")

    cursor.execute("""INSERT INTO teams (teamName, teamLeague, teamChampionsLeague, teamUefaLeague, teamCountry)
                                    VALUES('Chelsea', '2', true, false, '2')""")
    cursor.execute("""INSERT INTO teams (teamName, teamLeague, teamChampionsLeague, teamUefaLeague, teamCountry)
                                    VALUES('Manchester City', '2', true, false, '2')""")
    cursor.execute("""INSERT INTO teams (teamName, teamLeague, teamChampionsLeague, teamUefaLeague, teamCountry)
                                    VALUES('M. United', '2', true, false, '2')""")
    cursor.execute("""INSERT INTO teams (teamName, teamLeague, teamChampionsLeague, teamUefaLeague, teamCountry)
                                    VALUES('Tottenham', '2', true, false, '2')""")
    cursor.execute("""INSERT INTO teams (teamName, teamLeague, teamChampionsLeague, teamUefaLeague, teamCountry)
                                    VALUES('Liverpool', '2', false, true, '2')""")

    cursor.execute("""INSERT INTO teams (teamName, teamLeague, teamChampionsLeague, teamUefaLeague, teamCountry)
                                    VALUES('Beşiktaş', '3', true, false, '3')""")
    cursor.execute("""INSERT INTO teams (teamName, teamLeague, teamChampionsLeague, teamUefaLeague, teamCountry)
                                    VALUES('Galatasaray', '3', true, false, '3')""")
    cursor.execute("""INSERT INTO teams (teamName, teamLeague, teamChampionsLeague, teamUefaLeague, teamCountry)
                                    VALUES('Başakşehir', '3', true, false, '3')""")
    cursor.execute("""INSERT INTO teams (teamName, teamLeague, teamChampionsLeague, teamUefaLeague, teamCountry)
                                    VALUES('Kayserispor', '3', false, true, '3')""")
    cursor.execute("""INSERT INTO teams (teamName, teamLeague, teamChampionsLeague, teamUefaLeague, teamCountry)
                                    VALUES('Fenerbahçe', '3', false, true, '3')""")

    cursor.execute("""INSERT INTO teams (teamName, teamLeague, teamChampionsLeague, teamUefaLeague, teamCountry)
                                    VALUES('Bayern Münih', '4', true, false, '4')""")
    cursor.execute("""INSERT INTO teams (teamName, teamLeague, teamChampionsLeague, teamUefaLeague, teamCountry)
                                    VALUES('Schalke 04', '4', true, false, '4')""")
    cursor.execute("""INSERT INTO teams (teamName, teamLeague, teamChampionsLeague, teamUefaLeague, teamCountry)
                                    VALUES('RB Leipzig', '4', true, false, '4')""")
    cursor.execute("""INSERT INTO teams (teamName, teamLeague, teamChampionsLeague, teamUefaLeague, teamCountry)
                                    VALUES('Mgladbach', '4', false, true, '4')""")
    cursor.execute("""INSERT INTO teams (teamName, teamLeague, teamChampionsLeague, teamUefaLeague, teamCountry)
                                    VALUES('B. Dortmund', '4', false, true, '4')""")

    cursor.execute("""INSERT INTO teams (teamName, teamLeague, teamChampionsLeague, teamUefaLeague, teamCountry)
                                    VALUES('PSG', '5', false, true, '5')""")
    cursor.execute("""INSERT INTO teams (teamName, teamLeague, teamChampionsLeague, teamUefaLeague, teamCountry)
                                    VALUES('Monaco', '5', false, true, '5')""")
    cursor.execute("""INSERT INTO teams (teamName, teamLeague, teamChampionsLeague, teamUefaLeague, teamCountry)
                                    VALUES('Olympique Lyon', '5', false, true, '5')""")
    cursor.execute("""INSERT INTO teams (teamName, teamLeague, teamChampionsLeague, teamUefaLeague, teamCountry)
                                    VALUES('Marsilya', '5', false, true, '5')""")
    cursor.execute("""INSERT INTO teams (teamName, teamLeague, teamChampionsLeague, teamUefaLeague, teamCountry)
                                    VALUES('Nantes', '5', false, true, '5')""")

#leaguesposition table definition
    cursor.execute("""DROP TABLE IF EXISTS leaguePosition CASCADE""")
    cursor.execute("""CREATE TABLE leaguePosition(
                        id SERIAL PRIMARY KEY NOT NULL,
                        leagueName integer references leagues(id) ON DELETE RESTRICT ON UPDATE CASCADE,
                        teamName integer references teams(id) ON DELETE RESTRICT ON UPDATE CASCADE,
                        oynanan integer,
                        galibiyet integer,
                        beraberlik integer,
                        yenilgi integer,
                        atilanGol integer,
                        yenilenGol integer,
                        puan integer,
                        country integer references leagues(id) ON DELETE RESTRICT ON UPDATE CASCADE)""")

#leaguesposition table inserting data
    cursor.execute("""INSERT INTO leaguePosition (leagueName, teamName, oynanan, galibiyet, beraberlik, yenilgi, atilanGol, yenilenGol, puan, country)
                                    VALUES('1', '2', 12, 11, 1, 0, 33, 4, 34, '1')""")
    cursor.execute("""INSERT INTO leaguePosition (leagueName, teamName, oynanan, galibiyet, beraberlik, yenilgi, atilanGol, yenilenGol, puan, country)
                                    VALUES('1', '4', 12, 9, 3, 0, 32, 11, 30, '1')""")
    cursor.execute("""INSERT INTO leaguePosition (leagueName, teamName, oynanan, galibiyet, beraberlik, yenilgi, atilanGol, yenilenGol, puan, country)
                                    VALUES('1', '1', 12, 7, 3, 2, 22, 9, 24, '1')""")
    cursor.execute("""INSERT INTO leaguePosition (leagueName, teamName, oynanan, galibiyet, beraberlik, yenilgi, atilanGol, yenilenGol, puan, country)
                                    VALUES('1', '3', 12, 6, 6, 0, 16, 6, 24, '1')""")
    cursor.execute("""INSERT INTO leaguePosition (leagueName, teamName, oynanan, galibiyet, beraberlik, yenilgi, atilanGol, yenilenGol, puan, country)
                                    VALUES('1', '5', 12, 7, 1, 4, 14, 12, 22, '1')""")

    cursor.execute("""INSERT INTO leaguePosition (leagueName, teamName, oynanan, galibiyet, beraberlik, yenilgi, atilanGol, yenilenGol, puan, country)
                                    VALUES('2', '10', 12, 11, 1, 0, 40, 7, 34, '2')""")
    cursor.execute("""INSERT INTO leaguePosition (leagueName, teamName, oynanan, galibiyet, beraberlik, yenilgi, atilanGol, yenilenGol, puan, country)
                                    VALUES('2', '7', 12, 8, 2, 2, 27, 6, 26, '2')""")
    cursor.execute("""INSERT INTO leaguePosition (leagueName, teamName, oynanan, galibiyet, beraberlik, yenilgi, atilanGol, yenilenGol, puan, country)
                                    VALUES('2', '6', 12, 8, 1, 3, 23, 10, 25, '2')""")
    cursor.execute("""INSERT INTO leaguePosition (leagueName, teamName, oynanan, galibiyet, beraberlik, yenilgi, atilanGol, yenilenGol, puan, country)
                                    VALUES('2', '8', 12, 7, 2, 3, 20, 9, 23, '2')""")
    cursor.execute("""INSERT INTO leaguePosition (leagueName, teamName, oynanan, galibiyet, beraberlik, yenilgi, atilanGol, yenilenGol, puan, country)
                                    VALUES('2', '9', 12, 6, 4, 2, 24, 17, 22, '2')""")

    cursor.execute("""INSERT INTO leaguePosition (leagueName, teamName, oynanan, galibiyet, beraberlik, yenilgi, atilanGol, yenilenGol, puan, country)
                                    VALUES('3', '11', 12, 8, 2, 2, 27, 14, 26, '3')""")
    cursor.execute("""INSERT INTO leaguePosition (leagueName, teamName, oynanan, galibiyet, beraberlik, yenilgi, atilanGol, yenilenGol, puan, country)
                                    VALUES('3', '12', 12, 8, 2, 2, 23, 14, 26, '3')""")
    cursor.execute("""INSERT INTO leaguePosition (leagueName, teamName, oynanan, galibiyet, beraberlik, yenilgi, atilanGol, yenilenGol, puan, country)
                                    VALUES('3', '13', 12, 6, 4, 2, 19, 12, 22, '3')""")
    cursor.execute("""INSERT INTO leaguePosition (leagueName, teamName, oynanan, galibiyet, beraberlik, yenilgi, atilanGol, yenilenGol, puan, country)
                                    VALUES('3', '14', 12, 6, 4, 2, 19, 14, 22, '3')""")
    cursor.execute("""INSERT INTO leaguePosition (leagueName, teamName, oynanan, galibiyet, beraberlik, yenilgi, atilanGol, yenilenGol, puan, country)
                                    VALUES('3', '15', 12, 5, 5, 2, 25, 17, 20, '3')""")

    cursor.execute("""INSERT INTO leaguePosition (leagueName, teamName, oynanan, galibiyet, beraberlik, yenilgi, atilanGol, yenilenGol, puan, country)
                                    VALUES('4', '16', 12, 9, 2, 1, 30, 8, 29, '4')""")
    cursor.execute("""INSERT INTO leaguePosition (leagueName, teamName, oynanan, galibiyet, beraberlik, yenilgi, atilanGol, yenilenGol, puan, country)
                                    VALUES('4', '17', 12, 7, 2, 3, 16, 10, 23, '4')""")
    cursor.execute("""INSERT INTO leaguePosition (leagueName, teamName, oynanan, galibiyet, beraberlik, yenilgi, atilanGol, yenilenGol, puan, country)
                                    VALUES('4', '18', 12, 7, 2, 3, 20, 15, 23, '4')""")
    cursor.execute("""INSERT INTO leaguePosition (leagueName, teamName, oynanan, galibiyet, beraberlik, yenilgi, atilanGol, yenilenGol, puan, country)
                                    VALUES('4', '19', 12, 6, 3, 3, 21, 21, 21, '4')""")
    cursor.execute("""INSERT INTO leaguePosition (leagueName, teamName, oynanan, galibiyet, beraberlik, yenilgi, atilanGol, yenilenGol, puan, country)
                                    VALUES('4', '20', 12, 6, 2, 4, 29, 16, 20, '4')""")

    cursor.execute("""INSERT INTO leaguePosition (leagueName, teamName, oynanan, galibiyet, beraberlik, yenilgi, atilanGol, yenilenGol, puan, country)
                                    VALUES('5', '21', 13, 11, 2, 0, 43, 9, 35, '5')""")
    cursor.execute("""INSERT INTO leaguePosition (leagueName, teamName, oynanan, galibiyet, beraberlik, yenilgi, atilanGol, yenilenGol, puan, country)
                                    VALUES('5', '22', 13, 9, 2, 2, 35, 13, 29, '5')""")
    cursor.execute("""INSERT INTO leaguePosition (leagueName, teamName, oynanan, galibiyet, beraberlik, yenilgi, atilanGol, yenilenGol, puan, country)
                                    VALUES('5', '23', 13, 7, 5, 1, 32, 15, 26, '5')""")
    cursor.execute("""INSERT INTO leaguePosition (leagueName, teamName, oynanan, galibiyet, beraberlik, yenilgi, atilanGol, yenilenGol, puan, country)
                                    VALUES('5', '24', 13, 7, 4, 2, 27, 18, 25, '5')""")
    cursor.execute("""INSERT INTO leaguePosition (leagueName, teamName, oynanan, galibiyet, beraberlik, yenilgi, atilanGol, yenilenGol, puan, country)
                                    VALUES('5', '25', 13, 7, 2, 4, 12, 13, 23, '5')""")

#match table definition
    cursor.execute("""DROP TABLE IF EXISTS match CASCADE""")
    cursor.execute("""CREATE TABLE match(
                        id SERIAL PRIMARY KEY NOT NULL,
                        matchTime VARCHAR(30),
                        matchDate VARCHAR(30),
                        homeTeamId integer references teams(id) ON DELETE RESTRICT ON UPDATE CASCADE,
                        homeTeamScore integer,
                        guestTeam integer references teams(id) ON DELETE RESTRICT ON UPDATE CASCADE,
                        guestTamScore integer,
                        result integer)""")

#match table inserting data
    cursor.execute("""INSERT INTO match (matchTime, matchDate, homeTeamId, homeTeamScore, guestTeam, guestTamScore, result)
                                    VALUES('21:45' ,'22/11/2017', '1', 0, '2', 0, 0)""")
    cursor.execute("""INSERT INTO match (matchTime, matchDate, homeTeamId, homeTeamScore, guestTeam, guestTamScore, result)
                                    VALUES('21:45' ,'22/11/2017', '3', 0, '4', 0, 0)""")
    cursor.execute("""INSERT INTO match (matchTime, matchDate, homeTeamId, homeTeamScore, guestTeam, guestTamScore, result)
                                    VALUES('20:45' ,'22/11/2017', '5', 0, '6', 0, 0)""")
    cursor.execute("""INSERT INTO match (matchTime, matchDate, homeTeamId, homeTeamScore, guestTeam, guestTamScore, result)
                                    VALUES('20:45' ,'22/11/2017', '7', 0, '8', 0, 0)""")
    cursor.execute("""INSERT INTO match (matchTime, matchDate, homeTeamId, homeTeamScore, guestTeam, guestTamScore, result)
                                    VALUES('19:45' ,'22/11/2017', '9', 0, '10', 0, 0)""")
    cursor.execute("""INSERT INTO match (matchTime, matchDate, homeTeamId, homeTeamScore, guestTeam, guestTamScore, result)
                                    VALUES('19:45' ,'22/11/2017', '11', 2, '12', 1, 1)""")
    cursor.execute("""INSERT INTO match (matchTime, matchDate, homeTeamId, homeTeamScore, guestTeam, guestTamScore, result)
                                    VALUES('21:45' ,'21/11/2017', '13', 0, '14', 6, 2)""")
    cursor.execute("""INSERT INTO match (matchTime, matchDate, homeTeamId, homeTeamScore, guestTeam, guestTamScore, result)
                                    VALUES('21:45' ,'21/11/2017', '15', 2, '16', 1, 1)""")
    cursor.execute("""INSERT INTO match (matchTime, matchDate, homeTeamId, homeTeamScore, guestTeam, guestTamScore, result)
                                    VALUES('21:45' ,'21/11/2017', '17', 1, '18', 2, 2)""")
    cursor.execute("""INSERT INTO match (matchTime, matchDate, homeTeamId, homeTeamScore, guestTeam, guestTamScore, result)
                                    VALUES('21:45' ,'21/11/2017', '19', 0, '20', 5, 2)""")

#wager table definition
    cursor.execute("""DROP TABLE IF EXISTS wager CASCADE""")
    cursor.execute("""CREATE TABLE wager(
                        id SERIAL PRIMARY KEY NOT NULL,
                        matchId integer references match(id) ON DELETE RESTRICT ON UPDATE CASCADE,
                        userExpect integer,
                        wagerValue integer,
                        wagerWin BOOLEAN,
                        userId integer references users(id) ON DELETE RESTRICT ON UPDATE CASCADE)""")

#wager table inserting data
    cursor.execute("""INSERT INTO wager (matchId, userExpect, wagerValue, wagerWin, userId)
                                    VALUES('1', 1, 10, true, 1)""")
    cursor.execute("""INSERT INTO wager (matchId, userExpect, wagerValue, wagerWin, userId)
                                    VALUES('2', 1, 10, true, 2)""")
    cursor.execute("""INSERT INTO wager (matchId, userExpect, wagerValue, wagerWin, userId)
                                    VALUES('3', 1, 10, true, 3)""")
    cursor.execute("""INSERT INTO wager (matchId, userExpect, wagerValue, wagerWin, userId)
                                    VALUES('4', 1, 10, true, 4)""")
    cursor.execute("""INSERT INTO wager (matchId, userExpect, wagerValue, wagerWin, userId)
                                    VALUES('5', 1, 10, true, 5)""")