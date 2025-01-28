import jwt
import logging
import datetime
from datetime import timezone

from marshmallow import ValidationError

from flask import Blueprint, Response, jsonify, request

from backend.config import get_config
from backend.utils.decorators import jwt_required
from backend.external.schemas import AuthorizationSchema

logger = logging.getLogger(__name__)

auth = Blueprint("auth", __name__)

@auth.post('/authentication')
def login():
    """
    Autenticação simples

    Endepoint de geração de um token no formato JWT a partir das credenciais de um Auth Basic (username e password), do qual pode ser utilizado para validar as requisições de cada um dos endepoints.
    ---
    tags:
        - Auth
    security:
        - basicAuth: []
    responses:
        200:
            description: Success to create token
            schema:
                type: object
                properties:
                    exp:
                        type: string
                        format: date-time
                        description: entity_id of Entity
                    message:
                        type: string
                        description: message creation
                    token:
                        type: string
                        description: token JWT
        401:
            description: Token not created
    """
    try:
        config, env = get_config()
        schema = AuthorizationSchema()

        login = request.authorization.__dict__['parameters']
        
        # Validação dos campos
        schema.load(login)
        
        token = jwt.encode(
            {
                'aud': config.AUDIENCE,
                'username': login['username'], 
                'exp': datetime.datetime.now(tz=timezone.utc) + datetime.timedelta (minutes=15) 
            }, 
            key=config.SECRET_KEY, 
            algorithm='HS256'
        )
            
        return jsonify({'message': 'Validated successfully', 'token': token, 'exp': datetime.datetime.now() + datetime.timedelta (minutes=15)})
    except ValidationError as ve:
        return jsonify({ 'message': 'username or password is(are) missed', 'WWW-Authenticate': 'Basic auth="Login required"'}), 401
    except Exception as err:
        return jsonify({ 'message': 'could not verify', 'WWW-Authenticate': 'Basic auth="Login required"'}), 401

@auth.get('/test_decorator')
@jwt_required
def test(current_user):
    print(current_user)
    return "Token autenticado"