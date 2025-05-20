from flask import Flask, request
import mysql.connector

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        conn = mysql.connector.connect(host='db', user='user', password='pass', database='demo')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name) VALUES (%s)", (name,))
        conn.commit()
        cursor.close()
        conn.close()
        return "Data inserted!"
    return '''
        <form method="POST">
            Name: <input name="name">
            <input type="submit">
        </form>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
