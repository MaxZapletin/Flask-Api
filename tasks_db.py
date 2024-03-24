import json
all_tasks_file = "/home/max/Study/task_api_server/tasks.json"

# 1. Read file contents


def get_all_tasks():
    with open(all_tasks_file, "r") as file:
        all_tasks = json.load(file)
        return all_tasks

def get_specific_task():
    

# def add_task(task):
#     pass


# def delet_task(which_task):
#     pass


# def update_task():
#     pass
