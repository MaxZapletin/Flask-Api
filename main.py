import json
from flask import Flask, request

DB_FILE = "D:\Studying_DevOps_Bar_Ilan\Flask-Api\\tasks.json"

app = Flask(__name__)
# file path is global.
# all function works based on data and not file.
@app.route("/tasks/int:<user_id>", methods=["PUT"])
def update_user(user_id: int):
    data = read_db()
    data[str(user_id)] == request.get_json()
    write_db(data)
        
@app.route("/tasks", methods=["POST"])
def create_user(request_data: dict):
    data = read_db()
    user_id = str(len(data))
    data[user_id] = request_data
    write_db(data)

@app.route("tasks/int:<user_id>", methods=["DELETE"])
def delete_user(user_id: int):
    data = read_db()
    data[str(user_id)] = None
    write_db(data)

@app.route("/tasks", methods=["GET"])
def read_users():
    return read_db()

@app.route("/tasks/int:<user_id>", methods=["POST"])
def read_user(user_id: int):
    users = read_db()
    return users[str(user_id)]

def read_db():
    with open(DB_FILE, "r") as f:
        return json.load(f)
    
def write_db(data: dict):
    with open(DB_FILE, "w") as f:
        json.dump(data, f,indent=4)

