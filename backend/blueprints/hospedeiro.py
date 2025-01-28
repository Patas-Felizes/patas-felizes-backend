from flask import Blueprint, request, jsonify
from backend.services.hospedeiro_service import (
    list_hospedeiros_service,
    get_hospedeiro_service,
    create_hospedeiro_service,
    update_hospedeiro_service,
    delete_hospedeiro_service,
)

hospedeiro_bp = Blueprint("hospedeiro", __name__, url_prefix="/hospedeiros")


@hospedeiro_bp.route("/", methods=["GET"])
def list_hospedeiros():
    """
    Lista todos os hospedeiros armazenados no banco de dados.
    ---
    tags:
      - Hospedeiros
    definitions:
      HospedeiroSchema:
        type: object
        properties:
          hospedeiro_id:
            type: integer
          nome:
            type: string
          telefone:
            type: string
          email:
            type: string
          moradia:
            type: string
    responses:
        200:
            description: Lista de hospedeiros
            schema:
              type: array
              items:
                $ref: '#/definitions/HospedeiroSchema'
        404:
            description: Nenhum hospedeiro encontrado
    """
    response = list_hospedeiros_service()

    if response["status"] == 200:
        return jsonify(response["data"]), 200

    return jsonify({"message": response["message"]}), response["status"]


@hospedeiro_bp.route("/<int:hospedeiro_id>", methods=["GET"])
def get_hospedeiro(hospedeiro_id):
    """
    Retorna um hospedeiro específico do banco de dados.
    ---
    tags:
      - Hospedeiros
    parameters:
      - in: path
        name: hospedeiro_id
        type: integer
        required: true
    definitions:
      HospedeiroSchema:
        type: object
        properties:
          hospedeiro_id:
            type: integer
          nome:
            type: string
          telefone:
            type: string
          email:
            type: string
          moradia:
            type: string
    responses:
      200:
        description: Hospedeiro encontrado
        schema:
          $ref: '#/definitions/HospedeiroSchema'
      404:
        description: Hospedeiro não encontrado
    """
    response = get_hospedeiro_service(hospedeiro_id)

    if response["status"] == 200:
        return jsonify(response["data"]), 200

    return jsonify({"message": response["message"]}), response["status"]


@hospedeiro_bp.route("/", methods=["POST"])
def create_hospedeiro():
    """
    Cria um novo hospedeiro no banco de dados.
    ---
    tags:
      - Hospedeiros
    parameters:
      - in: body
        name: hospedeiro
        schema:
          $ref: '#/definitions/HospedeiroSchema'
    responses:
      201:
        description: Hospedeiro criado com sucesso
        schema:
          $ref: '#/definitions/HospedeiroSchema'
      400:
        description: Erro ao criar hospedeiro
    """
    hospedeiro_data = request.get_json()
    response = create_hospedeiro_service(hospedeiro_data)

    if response["status"] == 201:
        return jsonify(response["data"]), 201

    return jsonify({"message": response["message"]}), response["status"]


@hospedeiro_bp.route("/<int:hospedeiro_id>", methods=["PUT"])
def update_hospedeiro(hospedeiro_id):
    """
    Atualiza um hospedeiro específico do banco de dados.
    ---
    tags:
      - Hospedeiros
    parameters:
      - in: path
        name: hospedeiro_id
        type: integer
        required: true
      - in: body
        name: hospedeiro
        schema:
          $ref: '#/definitions/HospedeiroSchema'
    responses:
      200:
        description: Hospedeiro atualizado com sucesso
        schema:
          $ref: '#/definitions/HospedeiroSchema'
      400:
        description: Erro ao atualizar hospedeiro
    """
    hospedeiro_data = request.get_json()
    response = update_hospedeiro_service(hospedeiro_id, hospedeiro_data)

    if response["status"] == 200:
        return jsonify(response["data"]), 200

    return jsonify({"message": response["message"]}), response["status"]


@hospedeiro_bp.route("/<int:hospedeiro_id>", methods=["DELETE"])
def delete_hospedeiro(hospedeiro_id):
    """
    Deleta um hospedeiro específico do banco de dados.
    ---
    tags:
      - Hospedeiros
    parameters:
      - in: path
        name: hospedeiro_id
        type: integer
        required: true
    responses:
      204:
        description: Hospedeiro deletado com sucesso
      404:
        description: Hospedeiro não encontrado
    """
    response = delete_hospedeiro_service(hospedeiro_id)

    return jsonify({"message": response["message"]}), response["status"]
