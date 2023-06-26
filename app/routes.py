from flask import jsonify

from app import app
from app.service import get_value, set_value


@app.route('/get/<key>', methods=['GET'])
def get(key):
    value = get_value(key)
    return jsonify(value), 200


@app.route('/set/<key>/<value>', methods=['POST'])
def set(key, value):
    set_value(key, value)
    return jsonify({'message': 'Successfully set value'}), 200
