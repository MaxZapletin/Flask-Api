import json
from flask import jsonify, request

#all_tasks_file = "/home/max/Study/Flask-Api/tasks.json"
all_tasks_file = 'D:\Studying_DevOps_Bar_Ilan\Flask-Api\\tasks.json'


def get_all_tasks():
    with open(all_tasks_file, "r") as file:
        print(file)
        all_tasks = json.load(file)
        return all_tasks
#open json file wit ha lot of steps

def get_single_task(task_id):
    tasks = get_all_tasks()
    for task in tasks:
        if task["id"] == task_id:
            return task    
    return ({"message": "Task not found"})


def post_new_task(single_task):
    data = request.get_json()
    with open(all_tasks_file, 'r') as file:
        all_tasks = json.load(file)
        #task_id = len(all_tasks) + 1
        data["id"] == len(all_tasks) + 1
        #new_task = {'id': task_id,
                    #'title': data['title'], 'details': data['details']}
        all_tasks.append(data)
        json.dump(all_tasks, file, indent=4)
    return {"message": f"Task {data["id"]} added"}

def read_tasks():
    with open(all_tasks_file, "r") as f:
        return json.load(f)
    
config = read_config()
    if name in config["hosts"]:
        rprint(f"Host [bold]{name}[/bold] already exists")
        raise typer.Abort()

    config["hosts"][name] = {"ip": ip}

    write_config(config)
    rprint(f"Host [bold]{name}[/bold] added")
# @app.route("/tasks/<int:task_id>", methods=["POST"])
# def update_task(task_id):
#     data = request.get_json()
#     for all_tasks_file in tasks:
#         if task['id'] == task_id:
#             task['title'] = data.get('title', task['title'])
#             task['details'] = data.get('details', task['details'])
#             return json.dumps({"message": f"Task number {task_id} was updated"}), 200
#     return json.dumps({"message": "Task not found"})


# all_tasks = []


# def post_new_task2():
#     data = request.get_json()
#     with open(all_tasks_file, 'r+') as file:
#         json_read = json.load(file)
#         all_tasks = json_read['tasks']
#         tasks_id = len(all_tasks) + 1
#         new_task = {'id': tasks_id,
#                     'title': data['title'], 'details': data['details']}
#         all_tasks.append(new_task)
#         file.seek(0)
#         json.dump(all_tasks, file, indent=4)
#         file.truncate()
#     return {"message": f"Task {tasks_id} added"}


# def delete_task(which_task):
#     pass


# def update_task():
#     pass
