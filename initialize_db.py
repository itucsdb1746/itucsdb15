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



