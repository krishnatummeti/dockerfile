from flask import Flask
import redis

app = Flask(__name__)
redis_client = redis.StrictRedis(host='redis', port=6379, db=0)

@app.route('/')
def hello_world():
    redis_client.incr('hits')
    count = redis_client.get('hits').decode('utf-8')
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Visitor Counter | Tech Base Hub</title>
        <style>
            body {{
                margin: 0;
                padding: 0;
                height: 100vh;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(to right, #0055a5, #007BFF);
                color: #fff;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                text-align: center;
            }}
            header {{
                position: absolute;
                top: 0;
                width: 100%;
                padding: 20px 0;
                background-color: rgba(0, 0, 0, 0.2);
                font-size: 28px;
                font-weight: bold;
                box-shadow: 0 2px 4px rgba(0,0,0,0.2);
            }}
            main {{
                max-width: 600px;
                padding: 40px;
                background: rgba(255, 255, 255, 0.1);
                border-radius: 12px;
                box-shadow: 0 8px 16px rgba(0,0,0,0.3);
            }}
            h1 {{
                font-size: 36px;
                margin-bottom: 20px;
            }}
            .count {{
                font-size: 60px;
                color: #ffdd57;
                margin-top: 20px;
                font-weight: bold;
            }}
            footer {{
                position: absolute;
                bottom: 10px;
                font-size: 14px;
                color: #f0f0f0;
            }}
        </style>
    </head>
    <body>
        <header>🌐 Tech Base Hub</header>
        <main>
            <h1>Welcome to the Flask + Redis Counter App</h1>
            <p>This page has been visited:</p>
            <div class="count">{count} times</div>
        </main>
        <footer>© 2025 Tech Base Hub | All Rights Reserved</footer>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
