from flask import Flask
# from flask.wrappers import Request
from flasgger import Swagger
import os

# WSGI
app = Flask(__name__)
Swagger(app)

@app.route('/')
def welcome():
    return "Learning Swagger Building"



if __name__ == '__main__':
    port = int(os.environ.get('PORT',5000))
    app.run(host= '0.0.0.0', port=port)
