from flask import Flask, jsonify

app = Flask(__name__)

USERS = {
    1: {"id": 1, "username": "alice", "email": "alice@test.com", "role": "user"},
    2: {"id": 2, "username": "bob", "email": "bob@test.com", "role": "admin"}
}

@app.route("/users/<int:user_id>")
def get_user(user_id):
    return jsonify(USERS.get(user_id, {}))

if __name__ == "__name__":
    app.run(debug=True)