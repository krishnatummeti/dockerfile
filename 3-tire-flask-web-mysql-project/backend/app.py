from flask import Flask, request, render_template_string
import mysql.connector

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
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
        cursor.close()
        conn.close()

        return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Submission Successful</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #e8f4f8;
                    padding: 40px;
                    text-align: center;
                    color: #333;
                }
                h1 {
                    color: #2e8b57;
                }
                p {
                    font-size: 18px;
                }
                a {
                    text-decoration: none;
                    color: #2e8b57;
                    font-weight: bold;
                }
                a:hover {
                    color: #155d3f;
                }
            </style>
        </head>
        <body>
            <h1>Thank you, {{ name }}!</h1>
            <p>Your data has been submitted successfully.</p>
            <a href="/">Submit another response</a>
        </body>
        </html>
        ''', name=name)
    else:
        # Show a simple message or redirect from GET
        return "Flask backend is up. Use the HTML form to submit data."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
