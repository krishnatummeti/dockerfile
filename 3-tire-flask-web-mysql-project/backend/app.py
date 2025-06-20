from flask import Flask, request, render_template_string
import mysql.connector

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')

        if not name or not email:
            return "Error: Missing name or email field.", 400

        try:
            conn = mysql.connector.connect(
                host='my-mysql',
                user='root',
                password='root@123',
                database='Tech_Base_Hub_DB'
            )
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO submissions (name, email) VALUES (%s, %s)",
                (name, email)
            )
            conn.commit()
            print(f"✅ Successfully inserted: {name}, {email}")
        except Exception as e:
            print(f"❌ Error inserting into database: {e}")
            return "Internal Server Error: Could not save data.", 500
        finally:
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
        return '''
        <!DOCTYPE html>
        <html>
        <head><title>Flask App</title></head>
        <body>
            <h2>Flask backend is up.</h2>
            <p>Use the HTML form from the frontend to submit data.</p>
        </body>
        </html>
        '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
