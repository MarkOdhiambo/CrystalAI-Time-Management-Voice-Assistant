from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

TODOS = {
    '1': {'task': 'Build an API.'},
    '2': {'task': 'Go to and buy some shopping.'}
}

LOG = {
    '1': {'log': 'Crystal time-management project.'}
}

#Error handling for the todo list
def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('task',location='form')


# Todo
# shows a single todo item and lets you delete a todo item
class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201


# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys())) + 1
        # todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201

#Error handling for the todo list
def abort_if_log_doesnt_exist(log_id):
    if log_id not in LOG:
        abort(404, message="Todo {} doesn't exist".format(log_id))

logparser = reqparse.RequestParser()
logparser.add_argument('log')

# Activity log
# shows a single activity log item and lets you delete a log item
class Log(Resource):
    def get(self, log_id):
        abort_if_log_doesnt_exist(log_id)
        return LOG[log_id]

    def delete(self, log_id):
        abort_if_log_doesnt_exist(log_id)
        del LOG[log_id]
        return '', 204

    def put(self, log_id):
        args = logparser.parse_args()
        task = {'log': args['log']}
        LOG[log_id] = task
        return task, 201


# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class activityLog(Resource):
    def get(self):
        return LOG

    def post(self):
        args = logparser.parse_args()
        log_id = int(max(LOG.keys())) + 1
        # todo_id = 'todo%i' % todo_id
        LOG[log_id] = {'task': args['task']}
        return LOG[log_id], 201

##
## Actually setup the Api resource routing here
##
api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')

api.add_resource(activityLog, '/log')
api.add_resource(Log, '/log/<log_id>')


if __name__ == '__main__':
    app.run(debug=True)