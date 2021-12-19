from flask import Flask, render_template, request, redirect, url_for,Response
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)
todos = {}


class Todo(Resource):

    def get(self, todo_id):
        try:
            data = {todo_id: todos[todo_id]}
        except KeyError:
            return Response("Not found", status=404)
        return data

    def put(self, todo_id):
        todos[todo_id] = request.json.get('text')
        return {todo_id: todos[todo_id]}

    def delete(self, todo_id):
        del todos[todo_id]
        return Response(todos, status=204)


class TodoList(Resource):

    def get(self):
        return todos

    def post(self):
        todos[request.json.get('todo_id', None)] = request.json.get('text', "")
        return todos


api.add_resource(Todo, '/todos/<int:todo_id>')
api.add_resource(TodoList, '/todos')




if __name__ == "__main__":

    app.run(debug=True,host="0.0.0.0",port=4459)
