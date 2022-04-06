# HOST FILE

from flask import *

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
    def get(self, id, pw):
        return {"contents": get_like_contents(id, pw)}
