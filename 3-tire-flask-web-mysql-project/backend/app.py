from flask import Flask, request
import mysql.connector

app = Flask(__name__)

@app.route('/', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    conn = mysql.connector.connect(
        host='mysql',
        user='root',
        password='root',
        database='appdb'
    )
    cursor = conn.cursor()
    cursor.execute("INSERT INTO submissions (name, email) VALUES (%s, %s)", (name, email))
    conn.commit()
    return "Data Submitted!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
