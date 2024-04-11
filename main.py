import json
from flask import Flask, request, jsonify

DB_FILE = "./tasks.json"

app = Flask(__name__)


def read_db():
    try:
        with open(DB_FILE, "r") as file:
            data = json.load(file)
    except json.decoder.JSONDecodeError:
        data = {}
    return data


def write_db(data):
    with open(DB_FILE, "w") as file:
        json.dump(data, file, indent=4)


@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    tasks = read_db()
    if str(task_id) in tasks:
        tasks[str(task_id)].update(request.json)
        write_db(tasks)
        return jsonify({"Message": "The existing task was updated"})
    else:
        return jsonify({"error": "Task not found"})


@app.route("/tasks", methods=["POST"])
def create_task():
    tasks = read_db()
    new_task_id = str(len(tasks))
    new_task_data = request.json
    tasks[new_task_id] = new_task_data
    write_db(tasks)
    return jsonify({"message": "The new task was created successfully", "task_id": new_task_id})


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    tasks = read_db()
    if str(task_id) in tasks:
        del tasks[str(task_id)]
        write_db(tasks)
        return jsonify({"message": "The task was deleted successfully"})
    else:
        return jsonify({"error": "Task not found"})


@app.route("/tasks", methods=["GET"])
def read_tasks():
    return read_db()


@app.route("/tasks/<int:task_id>", methods=["GET"])
def read_task(task_id):
    tasks = read_db()
    if str(task_id) in tasks:
        return jsonify(tasks[str(task_id)])
    else:
        return jsonify({"error": "Task not found"})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
