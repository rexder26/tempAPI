# app.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/users', methods=['GET'])
def get_users():
    users = [
        {"id": 1, "name": "Nati"},
        {"id": 2, "name": "Nardi"},
        {"id": 3, "name": "Fitse"}
    ]
    return jsonify(users)

if __name__ == '__main__':
    app.run()
