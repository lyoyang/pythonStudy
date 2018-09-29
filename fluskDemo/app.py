from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/info/')
def info():
    # userInfo = {"name":"jim", "age":12, "msg":"userInfo"}
    return __name__

@app.route('/user/<username>')
def getUser(username):
    return 'I am ' + username

@app.route('/num/<int:post_id>')
def getNum(post_id):
    return 'the num is ' + str(post_id)


if __name__ == '__main__':
    app.debug = True
    app.run()
