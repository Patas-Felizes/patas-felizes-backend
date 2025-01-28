import jwt
import logging
import datetime
from datetime import timezone

from marshmallow import ValidationError
from flask import Blueprint, Response, jsonify, request

from backend.config import get_config
from backend.utils.decorators import jwt_required
from backend.external.model import UserModel
from backend.external.schemas import UserSchema
from backend.db import db

logger = logging.getLogger(__name__)

auth = Blueprint("auth", __name__)

@auth.route("/register", methods=["POST"])
def register():
    """
    Registra um novo usuário no banco de dados.
    ---
    tags:
      - Usuários
    definitions:
      UserSchema:
        type: object
        properties:
          username:
            type: string
          password:
            type: string
          email:
            type: string
        example:
          username: "seu_nome"
          password: "sua_senha"
          email: "seu_email@gmail.com"
    parameters:
      - in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/UserSchema'
    responses:
      201:
        description: Usuário criado com sucesso
      400:
        description: Erro ao criar usuário
    """
    logger.info("Registrando usuário")
    try:
        data = request.get_json()
        schema = UserSchema()
        user_data = schema.load(data)
    except ValidationError as e:
        logger.error("Erro ao registrar usuário, dados inválidos")
        return jsonify({"erro": e.messages}), 400
    except Exception as e:
        logger.error(f"Erro inesperado ao processar dados de registro: {str(e)}")
        return jsonify({"erro": "Erro interno ao processar registro"}), 500

    new_user = UserModel(
        username=user_data["username"],
        password="",
        email=user_data["email"]
    )
    
    new_user.set_password(user_data["password"])

    db.session.add(new_user)
    db.session.commit()

    logger.info("Usuário registrado com sucesso")
    return jsonify({"mensagem": "Usuário criado com sucesso"}), 201

@auth.route("/login", methods=["POST"])
def login():
    """
    Autentica um usuário e gera um token JWT.
    ---
    tags:
      - Usuários
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            email:
              type: string
            password:
              type: string
          example:
            email: "seu_email@gmail.com"
            password: "sua_senha"
    responses:
      200:
        description: Usuário autenticado com sucesso
      400:
        description: Email ou senha inválidos
      404:
        description: Usuário não encontrado
    """
    logger.info("Autenticando usuário")
    data = request.get_json()

    if not isinstance(data, dict):
        logger.error("Dados de entrada inválidos")
        return jsonify({"mensagem": "Dados de entrada inválidos"}), 400

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        logger.error("Email ou senha não fornecidos")
        return jsonify({"mensagem": "Email e senha são obrigatórios"}), 400

    try:
        db_user = UserModel.query.filter_by(email=email).first()
        if not db_user:
            logger.error(f"Usuário com email {email} não encontrado.")
            return jsonify({"mensagem": "Usuário não encontrado"}), 404

        if not db_user.check_password(password):
            logger.error("Senha inválida.")
            return jsonify({"mensagem": "Senha inválida"}), 400

        config, _ = get_config()
        token = jwt.encode(
            {
                "user_id": db_user.user_id,
                "exp": datetime.datetime.now(timezone.utc) + datetime.timedelta(hours=999)
            },
            config.SECRET_KEY
        )

        logger.info("Usuário autenticado com sucesso")
        return jsonify({"token": token}), 200

    except ValidationError as e:
        logger.error("Erro de validação ao autenticar usuário")
        return jsonify({"erro": e.messages}), 400

    except Exception as e:
        logger.error(f"Erro inesperado ao autenticar usuário: {str(e)}")
        return jsonify({"mensagem": "Erro interno do servidor"}), 500