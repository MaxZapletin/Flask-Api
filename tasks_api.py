from flask import Flask, request
import json
import tasks_db

app = Flask(__name__)


@app.route("/tasks", methods=["GET"])
def get_all_tasks():
    all_tasks = tasks_db.get_all_tasks()
    return json.dumps({'tasks': all_tasks})


@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_single_task(task_id):
    single_task = tasks_db.get_single_task(task_id)
    return json.dumps(single_task)


@app.route("/tasks/<int:task_id>", methods=["GET", "POST"])
def add_task():
    new_task = tasks_db.post_new_task2()
    return json.dumps(new_task)


# @app.route("/tasks/<int:task_id>", methods=["PUT"])
# def update_task(task_id):
#     data = request.get_json()
#     for task in tasks:
#         if task['id'] == task_id:
#             task['title'] = data.get('title', task['title'])
#             task['details'] = data.get('details', task['details'])
#             return json.dumps({"message": f"Task number {task_id} was updated"}), 200
#     return json.dumps({"message": "Task not found"}),


# @app.route("/tasks/<int:task_id>", methods=["DELETE"])
# def delete_task(task_id):
#     for task in tasks:
#         if task['id'] == task_id:
#             tasks.remove(task)
#             return json.dumps({"message": f"Task number {task_id} was deleted"}), 200
#     return json.dumps({"message": "Task not found"}),

if __name__ == '__main__':
    app.run(port=5000)
