#flask app created with tutorial from https://www.geeksforgeeks.org/mysql-database-files/#

from flask import Flask, render_template
from flask.ext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'jay'
app.config['MYSQL_DATABASE_PASSWORD'] = 'jay'
app.config['MYSQL_DATABASE_DB'] = 'BookFinder'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)


conn = mysql.connect()
cursor = conn.cursor()

#cursor.callproc('sp_createUser',(_name,_email,_hashed_password))

#data = cursor.fetchall()

#if len(data) is 0:
#    conn.commit()
#    return json.dumps({'message':'User created successfully !'})
#else:
#    return json.dumps({'error':str(data[0])})

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()

