from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

TODOS = [
    {'id':1,'task': 'Build an API'},
    {'id':2,'task': 'Write my documentation'},
    {'id':3,'task': 'Profit!'}
]

LOG = [
    {'id':1,'log': 'Crystal time-management project.'}
]
REMAINDER = [
    {"id":1,'remainder': 'Build an API.',"date":"2012-11-23","time":"one"},
    {"id":2,'remainder': 'Get some shopping.',"date":"2012-11-23","time":"one"}
]

parser = reqparse.RequestParser()
parser.add_argument('task',location='form')

# Todo
# shows a single todo item and lets you delete a todo item
class Todo(Resource):
    def get(self, todo_id):
        todo_id=int(todo_id)
        for todo in TODOS:
            if todo_id==todo['id']:
                return todo

    def delete(self, todo_id):
        todo_id=int(todo_id)
        for todo in TODOS:
            if todo_id==todo['id']:
                index=TODOS.index(todo)
                del TODOS[index]
        return '', 204

# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        todoVal=TODOS[-1]
        id=todoVal['id']+1
        todo = {'id':id,'task': args['task']}
        TODOS.append(todo)
        return todo, 201

logparser = reqparse.RequestParser()
logparser.add_argument('log',location='form')

# Log
# shows a single log item and lets you delete a log item
class Log(Resource):
    def get(self, log_id):
        log_id=int(log_id)
        for log in LOG:
            if log_id==log['id']:
                return log

    def delete(self, log_id):
        log_id=int(log_id)
        for log in LOG:
            if log_id==log['id']:
                del LOG[log_id]
        return '', 204


# activityLog
# shows a list of all logs, and lets you POST to add new logs
class activityLog(Resource):
    def get(self):
        return LOG

    def post(self):
        args = logparser.parse_args()
        logVal=LOG[-1]
        id=logVal['id']+1
        log = {'id':id,'log': args['log']}
        LOG.append(log)
        return log, 201

remparser = reqparse.RequestParser()
remparser.add_argument('remainder',location='form')
remparser.add_argument('date',location='form')
remparser.add_argument('time',location='form')

# Remainder
# shows a single remainder item and lets you delete a remainder item
class Remainder(Resource):
    def get(self, rem_id):
        rem_id=int(rem_id)
        for rem in REMAINDER:
            if rem_id==rem['id']:
                return rem

    def delete(self, rem_id):
        rem_id=int(rem_id)
        for rem in REMAINDER:
            if rem_id==rem['id']:
                del REMAINDER[rem_id]
        return '', 204

# remainderList
# shows a list of all remainder, and lets you POST to add new remainders
class RemainderList(Resource):
    def get(self):
        return REMAINDER

    def post(self):
        args = remparser.parse_args()
        remainderVal=REMAINDER[-1]
        remid=remainderVal['id']+1
        remainder = {"id":remid,'remainder': args['remainder'],'time': args['time'],'date': args['date']}
        REMAINDER.append(remainder)
        return remainder, 201
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