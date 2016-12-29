#!flask/bin/python
from flask import Flask, jsonify, abort
from flask import make_response
from flask import url_for
from mysqlconn import conn


app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': '404 Not found'}), 404)

@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = filter(lambda t: t['id'] == task_id, tasks)
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})




if __name__ == '__main__':
    app.run(debug=True)
