# HOST FILE

from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

def loginMethod(id, pw):
    return True

def get_like_contents(id, pw):
    if loginMethod(id, pw) == True:
        return ["test"]
    else:
        return {"message": "id, pw is not correct.", "error": True}

@app.route('/api/v1/like_contents')
def like_contents():
    def post(self):
        global id
        global pw
        return {"contents": get_like_contents(id, pw)}
