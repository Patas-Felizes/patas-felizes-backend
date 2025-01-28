from functools import wraps
from flask import jsonify, request

from backend.utils.auth import validate_token

def jwt_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            return jsonify({'message':'token is missing','data':{}}), 401
        
        try:
            bearer, token = token.split(" ")

            if bearer.strip() != "Bearer":
                return jsonify({"message": "Token is invalid", "error": "Invalid Bearer token"}), 401
            
            is_valid, payload = validate_token(token)

            if is_valid:
                return f(payload, *args, **kwargs)
            
            return jsonify(payload), 401
        except Exception as err:
            return jsonify({"message": "Token is invalid", "error": str(err)}), 401
        
    return decorated
