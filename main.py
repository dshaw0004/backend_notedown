import os

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin

from fstore import add_new_message, get_all_message



app = Flask(__name__)
CORS(app, resources={
    r'/getallmsg': {
        "origins": ['*']
    },
    r'/addnewmsg': {
        "origins": ['*']
    },
    r'/': {
        "origins": [
            "*"
        ]
    },
    r'/login': {
        "origins": [
            "*"
        ]
    }
})


@app.route("/")
def index():
    return {
        'username': 'dshaw0004',
        'portfolio': 'https://dshaw0004.netlify.app',
        'fullname': 'Dipankar Shaw',
        'linkedin': 'https://www.linkedin.com/in/dshaw0004',
        'twitter': 'https://twitter.com/dshaw0004',
        'github': 'https://github.com/dshaw0004'
    }


@app.route("/getalltodo")
def getalltodo():
    auth = request.headers.get('Authorization')
    if auth == os.getenv('AUTH'):
        allmess = get_all_message()
        return jsonify(allmess)
    else:
        return jsonify({"permission": "denied"}), 404

@app.route("/addnewtodo", methods=['POST'])
def addnewtodo():
    data = request.json
    add_new_message(data.get('title'), data.get('description'))
    return {
        'title': data.get('title'),
        'description': data.get('description'),

    }



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6969)
