from flask import Flask, request, jsonify
import json

app = Flask(__name__)

all_taks_1 = {
    1: {'title': 'buy', 'description': 'milk'},
    2: {'title': 'buy', 'description': 'bread'},
    3: {'title': 'buy', 'description': 'coffee'}
}

all_taks_2 = {
    {'id': 1, 'title': 'buy', 'description': 'milk'},
    {'id': 2, 'title': 'buy', 'description': 'bread'},
    {'id': 3, 'title': 'buy', 'description': 'coffee'}
}

all_taks_3 = [
    [1, 'buy', 'milk'],
    [2, 'buy', 'bread'],
    [3, 'buy', 'coffee']
]
# >>> [   item[2]  for item in all_taks_3]
# ['milk', 'bread', 'coffee']


@app.route("/demo")
def get_demo():
    data = '("key" : "value)'
    return data


@app.route("/demo", methods=["POST"])
def add_demo():
    temp = request.data
    return ''


app.run()
