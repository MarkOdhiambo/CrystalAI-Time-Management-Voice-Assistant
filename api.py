
from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy

#Initializing the flask app
app= Flask(__name__)

#Setting up the database configurations
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
db=SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    todo = db.Column(db.String(160),nullable=False )
    def __repr__(self):
        return f"{self.todo}"

@app.route("/",methods=["GET","POST"])
def index():
    if(request.method == "POST"):
        some_json=request.get_json()
        return jsonify({'you sent':some_json}),201
    else:
        return jsonify({"about":"Hello world 2"})
    
@app.route('/todo',methods=['GET'])
def get_todo():
    return jsonify({'result'})


if __name__=='__main__':
    app.run(debug=True)
    