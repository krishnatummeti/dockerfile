from flask import Flask
import redis

app = Flask(__name__)
redis_client = redis.StrictRedis(host='redis', port=6379, db=0)

@app.route('/')
def hello_world():
    redis_client.incr('hits')
    return f'Hello, World! You have visited this page {redis_client.get("hits").decode("utf-8")} times.\n'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
