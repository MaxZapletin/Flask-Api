import json
from flask import Flask, request, jsonify

# DB_FILE = "D:\Studying_DevOps_Bar_Ilan\Flask-Api\\tasks.json"
DB_FILE = "/home/max/Study/Flask-Api/tasks.json"

app = Flask(__name__)
# file path is global.
# all function works based on data and not file.


def read_db():
    with open(DB_FILE, "r") as file:
        return json.load(file)


def write_db(data):
    with open(DB_FILE, "w") as file:
        json.dump(data, file, indent=4)


@app.route("/tasks/int:<task_id>", methods=["PUT"])
def update_task(task_id):
    data = read_db()
    data[str(task_id)] = request.get_json()
    write_db(data)


@app.route("/tasks", methods=["POST"])
def create_task(request_data):
    data = read_db()
    task_id = str(len(data))
    data[task_id] = request_data
    write_db(data)


@app.route("/tasks/int:<task_id>", methods=["DELETE"])
def delete_task(task_id):
    data = read_db()
    data[str(task_id)] = None
    write_db(data)


@app.route("/tasks", methods=["GET"])
def read_all_tasks():
    return read_db()


@app.route("/tasks/int:<task_id>", methods=["GET"])
def read_task(task_id):
    tasks = read_db()
    return read_task.tasks[str(task_id)]


if __name__ == '__main__':
    app.run(port=5000)
