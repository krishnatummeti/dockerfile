from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    connection = mysql.connector.connect(
        host="my-mysql",  # Corrected from 'mysql-db'
        user="root",
        password="root@123",
        database="Tech_Base_Hub_DB"
    )
    return connection

@app.route('/')
def hello_world():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT 'Hello, Docker! This is - Tech Base Hub'")
    result = cursor.fetchone()
    connection.close()
    
    return render_template('index.html', message=result[0])

if __name__ == "__main__":
    app.run(host='0.0.0.0')
