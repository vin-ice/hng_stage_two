#!/usr/bin/python3
"""Simple api for accessing person data"""
from flasgger import Swagger
from flasgger.utils import swag_from
from flask_cors import CORS
from flask import (
                   Flask, Response, Request,
                   request, make_response, jsonify, abort
    )
from models.user import User
from typing import TYPE_CHECKING

app = Flask(__name__)
CORS(app)
swagger = Swagger(app)


@app.route('/api', methods=['POST'], strict_slashes=False)
@swag_from('documentation/post_user.yml')
def add_user() -> Response:
    """creates user"""
    if request.is_json:
        req: Request = request.get_json()
        if 'name' in req:
            if 'value' in req:
                user: User = User(**req)
                user.save()
                return make_response(jsonify(user.to_dict()), 201)
            else:
                abort(400, 'Missing value')
        else:
            abort(400, "Missing Name")
    else:
        abort(400, "Not a JSON")


@app.route('/api/<user_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/get_user.yml')
def get_user(user_id):
    """retrieves user data"""
    user: User = User.from_store(user_id=user_id)
    if user is None:
        abort(404, {})
    else:
        return make_response(jsonify(user.to_dict()), 200)


@app.route('/api/<user_id>', methods=['PUT'], strict_slashes=False)
@swag_from('documentation/update_user.yml')
def update_user(user_id):
    """updates user data"""
    if request.is_json:
        req: Request = request.get_json()
        user: User = User.from_store(user_id)
        if user is not None:
            for k, v in req.items():
                if k not in ['user_id']:
                    setattr(user, k, v)
            user.update()
            return make_response(jsonify(user.to_dict()), 200)
        abort(404, "User does not exist")
    abort(404, 'Not a JSON')


@app.route('/api/<user_id>', methods=['DELETE'],
           strict_slashes=False)
@swag_from('documentation/delete_user.yml')
def delete_user(user_id):
    """delete users entry"""
    user = User.from_store(user_id)
    if user is not None:
        user.delete()
        return make_response(jsonify({}), 200)
    abort(400, 'User does not exist!')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
