from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def get(self, task_id=None):
    if task_id:
        for task in tasks:
            if task['id'] == task_id:
                return task, 200
        return {"message": "Task not found"}, 404
    return tasks, 200

def post(self):
    data = request.get_json()
    task_id = len(tasks) + 1
    task = {'id': task_id,
            'title': data['title'], 'description': data['description']}
    tasks.append(task)
    return task, 201

def put():
    

def delete(self, task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return {"message": f"Task {task_id} deleted"}, 200
