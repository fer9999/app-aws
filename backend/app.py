#!/bin/env python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
##################################################################
# Define a simple model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    

    def __repr__(self):
        return '<Todo %r>' % self.name

def db_create(todo):
    with app.app_context():
        db.session.add(todo)
        db.session.commit()

def db_read():
    with app.app_context():
        todo = Todo.query.all()
    todo=[i.__dict__ ["name"] for i in todo ]
    return todo

def db_update(todo_old, todo_new):
    with app.app_context():
        #todo.verified = True
        Todo.query.filter_by(name=todo_old).update(dict(name=todo_new))
        db.session.commit()

def db_delete(todo):
    with app.app_context():
        db.session.delete(todo)
        db.session.commit()

##################################################################




# Create the database tables
with app.app_context():
    db.create_all()
    
# CRUD/API
todo = ["todo 1", "todo 2"]

def createtest():
   todo=Todo(name="todo3")
   db_create(todo)

@app.route('/create', methods=['POST'])
def create():
    if request.is_json:
       data = request.json 
       # add todo
       todo=Todo(name=data['todo'])
       try:
         db_create(todo)
         return jsonify({'msg': "succeed"}), 200
       except:
         return jsonify({'msg': "fail"}), 400

    else:
       return jsonify({'error': 'Request must be in JSON format'}), 400

@app.route('/read', methods=['GET'])
def read():
    if request.method == 'GET':
        result= db_read()
        return jsonify({'msg': result}), 200
        


    return jsonify({'error': 'Request must be in JSON format'}), 400

@app.route('/test', methods=['POST'])
def test():
    data = request.json
    return jsonify({'message': 'This is a POST request', 'data': data}), 200


@app.route('/update', methods=['PUT'])
def update():
    if request.is_json:
      # TODO read from db 
      # if the old entry exist in db you need to replace it with new entry
      
      data = request.json
      for i in db_read():
        
        if data['todo_old'] == i:
          
            db_update(data['todo_old'], data['todo_new'])
            return jsonify({'message': 'This is a POST request', 'data': data['todo_new']}), 200

        else:
            return jsonify({'error': 'todo_old not in db'}), 400
    else:
      return jsonify({'error': 'Request must be in JSON format'}), 400


@app.route('/delete', methods=['DELETE'])
def delete():
    if request.is_json:
      # TODO DELETE FROM DB
      # 
       data = request.json
       
       # todo manage error
       try:
         db_delete(todo)
       except Exception as EX:
         print(EX)
         return jsonify({'error': f"{EX}"}), 404
       return jsonify({'message': todo}), 200
    else:
       return jsonify({'error': 'Request must be in JSON format'}), 400

if __name__ == '__main__':
   #createtest()
   app.run(debug=True, host="0.0.0.0")


