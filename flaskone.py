from flask import Flask

flaskone=Flask(__name__)

@flaskone.route('/')





@flaskone.route('/about')

def about():
    return '<h1> madurai</h1>'

@flaskone.route('/index/<name>')

def index(name):
    return "<h1>sathish {}</h1>".formate(name)


if __name__=="__main__":
    flaskone.run(debug=True)

