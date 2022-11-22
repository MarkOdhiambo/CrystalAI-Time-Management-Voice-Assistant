from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

TODOS = {
    "1": {'task': 'Build an API.'},
    "2": {'task': 'Go to and buy some shopping.'}
}
REMAINDER = {
    "1": {'remainder': 'Build an API.',"date":"2012-11-23","time":"one"},
    "2": {'remainder': 'Get some shopping.',"date":"2012-11-23","time":"one"}
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
        TODOS[todo_id] = {"task": args['task']}
        return TODOS[todo_id], 201

#Error handling for the todo list
def abort_if_log_doesnt_exist(log_id):
    if log_id not in LOG:
        abort(404, message="Log {} doesn't exist".format(log_id))

logparser = reqparse.RequestParser()
logparser.add_argument('log',location='form')

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

# Activity log
# shows a list of all logs, and lets you POST to add new log
class activityLog(Resource):
    def get(self):
        return LOG

    def post(self):
        args = logparser.parse_args()
        log_id = int(max(LOG.keys())) + 1
        log_id = str(log_id)
        LOG[log_id] = {'log': args['log']}
        return LOG[log_id], 201

#Error handling for the remainder
def abort_if_log_doesnt_exist(rem_id):
    if rem_id not in REMAINDER:
        abort(404, message="Remainder {} doesn't exist".format(rem_id))

remparser = reqparse.RequestParser()
remparser.add_argument('remainder',location='form')
remparser.add_argument('date',location='form')
remparser.add_argument('time',location='form')

# Remainder
# shows a single activity log item and lets you delete a log item
class Remainder(Resource):
    def get(self, rem_id):
        abort_if_log_doesnt_exist(rem_id)
        return REMAINDER[rem_id]

    def delete(self, rem_id):
        abort_if_log_doesnt_exist(rem_id)
        del REMAINDER[rem_id]
        return '', 204

    def put(self, rem_id):
        args = remparser.parse_args()
        task = {'remainder': args['remainder'],'time': args['time'],'date': args['date']}
        REMAINDER[rem_id] = task
        return task, 201


# Remainder List
# shows a list of all logs, and lets you POST to add new remainder
class RemainderList(Resource):
    def get(self):
        return REMAINDER

    def post(self):
        args = remparser.parse_args()
        rem_id = int(max(REMAINDER.keys())) + 1
        rem_id = str(rem_id)
        task = {'remainder': args['remainder'],'time': args['time'],'date': args['date']}
        REMAINDER[rem_id] = task
        return LOG[rem_id], 201

##
## Actually setup the Api resource routing here
##
api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')

api.add_resource(activityLog, '/log')
api.add_resource(Log, '/log/<log_id>')

api.add_resource(RemainderList, '/remainder')
api.add_resource(Remainder, '/remainder/<rem_id>')


if __name__ == '__main__':
    app.run(debug=True)