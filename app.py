from flask import Flask
from flask import render_template
from tinydb import TinyDB
import os

app = Flask(__name__)


def js_list():
    s = ""
    for x in os.listdir():
        if x.endswith(".json") and os.path.splitext(x)[0] not in ['F_TickSize', 'UserSendTo']:
            s = s + f'<p><a href="user/{os.path.splitext(x)[0]}">Open {x}</a></p>'
    return s


@app.route('/', methods=['GET'])
def index():
    res = js_list()
    if res == "":
        j = f'<!DOCTYPE html><html><body><h1>No Json File Available</h1></body></html>'
    else:
        j = f'<!DOCTYPE html><html><body><h1>Available Json Files</h1> {res}</body></html>'
    return j


@app.route('/user/<name>', methods=['GET'])
def user_view(name):
    if os.path.exists(f'{name}.json'):
        j = TinyDB(f'{name}.json').table('openPS').all()
        p = TinyDB(f'{name}.json').table('posPNL').all()
        print(j)
        print(p)
        return render_template('in.html', jdata=j, pdata=p, username=str(name).upper())
    else:
        return f"<h1>User {name} not found.</h1>"
