from flask import Flask


# WSGI
app = Flask(__name__)


@app.route('/')
def welcome():
    return "Learning Swagger Building"



if __name__ == "__main__":
    app.run()
