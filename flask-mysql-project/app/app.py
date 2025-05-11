from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    connection = mysql.connector.connect(
        host="mysql-db",  # Name of the MySQL container
        user="root",
        password="example",  # Password set in Docker
        database="test_db"  # Database created in MySQL
    )
    return connection

@app.route('/')
def hello_world():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT 'Hello, Docker! This is - Tech Base Hub'")
    result = cursor.fetchone()
    connection.close()
    
    # Render the index.html file and pass the 'message' variable
    return render_template('index.html', message=result[0])

if __name__ == "__main__":
    app.run(host='0.0.0.0')
