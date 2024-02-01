from flask import Flask, request
from uuid import uuid4

app = Flask(__name__)

users = {
    '1': {
        'first_name': 'Rico',
        'last_name': 'Uchiha',
        'email': 'him@mail.com',
        'password': '123'
    },
    '2': {
        'first_name': 'Max',
        'last_name': 'Zaturi',
        'email': 'who@mail.com',
        'password': '1256'
    }
}

cars = {
    '1': {
        'year': '2019',
        'make': 'Dodge',
        'model': 'Ram TRX',
        'user_id': '1'
    },
    '2': {
        'year': '2009',
        'make': 'Infiniti',
        'model': 'G37S',
        'user_id': '2'
    }
}
# user routes
@app.get('/user')
def user():
    return{'users': list(users.values())}, 200

@app.post('/user')
def create_user():
    json_body = request.get_json()
    users[uuid4()] =json_body
    return{ 'message ' : f'{json_body['username']} created' }, 201

