import json
all_tasks_file = "/home/max/Study/task_api_server/tasks.json"

# 1. Read file contents


def get_all_tasks():
    with open(all_tasks_file, "r") as file:
        all_tasks = json.load(file)
        return all_tasks


# def get_all_tasks():
#     pass


# def add_task(task):
#     pass


# def delet_task(which_task):
#     pass


# def update_task():
#     pass


# app = Flask("tasks")

# all_tasks = [
#     None,
#     {'id': 1, 'title': 'shop', 'details': 'Milk'},
#     {'id': 2, 'title': 'shop', 'details': 'Milk2'},
#     {'id': 3, 'title': 'shop', 'details': 'Milk3'},
#     {'id': 4, 'title': 'shop', 'details': 'Milk4'},
# ]


# @app.route("/tasks/")
# def get_all_tasks():
#     return json.dumps(all_tasks)


# @app.route("/tasks/<int:task_id>")
# def get_single_task(task_id):
#     del all_tasks[int(task_id)]
#     return json.dumps('deleted')


# if __name__ == '__main__':
#     app.run(port=5000)


# app = Flask(__name__)

# tasks = []


# @app.route("/tasks", methods=["GET"])
# def get_all_tasks():
#     return json.dumps({'tasks': tasks})


# @app.route("/tasks/<int:task_id>", methods=["GET"])
# def get_task(task_id):
#     for task in tasks:
#         if task['id'] == task_id:
#             return json.dumps(task)
#     return json.dumps({"message": "Task not found"})


# @app.route("/tasks", methods=["POST"])
# def add_task():
#     data = request.get_json()
#     tasks_id = len(tasks) + 1
#     task = {'id': tasks_id, 'shop': data['shop'], 'details': data['details']}
#     tasks.append(task)
#     return json.dumps({"message": f"Task number {tasks_id} was added"})

# @app.route("/")
# def delete():


# if __name__ == '__main__':
#     app.run(port=5000)
