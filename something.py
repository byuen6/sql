import MySQLdb

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="password",  # your password
                     db="menagerie")        # name of the data base


cur = db.cursor()

cur.execute("select name, birth, MONTH(birth) from pet")
for row in cur.fetchall():
    print (row)

db.close()