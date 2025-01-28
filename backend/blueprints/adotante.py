from flask import Blueprint, request, jsonify
from backend.services.adotante_service import (
    list_adotantes_service,
    get_adotante_service,
    create_adotante_service,
    delete_adotante_service,
    update_adotante_service
)

adotante_bp = Blueprint("adotante", __name__, url_prefix="/adotantes")

@adotante_bp.route("/", methods=["GET"])
def list_adotantes():
    """
    Lista todos os adotantes armazenados no banco de dados.
    ---
    tags:
      - Adotantes
    definitions:
      AdotanteSchema:
        type: object
        properties:
          adotante_id:
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
        description: Lista de adotantes
        schema:
          type: array
          items:
            $ref: '#/definitions/AdotanteSchema'
      404:
        description: Nenhum adotante encontrado no banco de dados.
    """
    response = list_adotantes_service()

    if response["status"] == 200:
        return jsonify(response["data"])

    return jsonify({"message": response["message"]}), response["status"]


@adotante_bp.route("/<int:adotante_id>", methods=["GET"])
def get_adotante(adotante_id):
    """
    Retorna um adotante específico do banco de dados.
    ---
    tags:
      - Adotantes
    parameters:
      - in: path
        name: adotante_id
        type: integer
        required: true
    definitions:
      AdotanteSchema:
        type: object
        properties:
          adotante_id:
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
        description: Adotante encontrado
        schema:
          $ref: '#/definitions/AdotanteSchema'
      404:
        description: Adotante não encontrado
    """
    response = get_adotante_service(adotante_id)

    if response["status"] == 200:
        return jsonify(response["data"])

    return jsonify({"message": response["message"]}), response["status"]


@adotante_bp.route("/", methods=["POST"])
def create_adotante():
    """
    Cria um novo adotante no banco de dados.
    ---
    tags:
      - Adotantes
    parameters:
      - in: body
        name: adotante
        schema:
          $ref: '#/definitions/AdotanteSchema'
    responses:
      201:
        description: Adotante criado com sucesso
        schema:
          $ref: '#/definitions/AdotanteSchema'
      400:
        description: Erro ao criar adotante
    """
    adotante_data = request.get_json()
    response = create_adotante_service(adotante_data)

    if response["status"] == 201:
        return jsonify(response["data"]), response["status"]

    return jsonify({"message": response["message"]}), response["status"]


@adotante_bp.route("/<int:adotante_id>", methods=["DELETE"])
def delete_adotante(adotante_id):
    """
    Deleta um adotante específico do banco de dados.
    ---
    tags:
      - Adotantes
    parameters:
      - in: path
        name: adotante_id
        type: integer
        required: true
    responses:
      204:
        description: Adotante deletado com sucesso
      404:
        description: Adotante não encontrado
    """
    response = delete_adotante_service(adotante_id)
    return jsonify({"message": response["message"]}), response["status"]


@adotante_bp.route("/<int:adotante_id>", methods=["PUT"])
def update_adotante(adotante_id):
    """
    Atualiza um adotante específico no banco de dados.
    ---
    tags:
      - Adotantes
    parameters:
      - in: path
        name: adotante_id
        type: integer
        required: true
      - in: body
        name: adotante
        schema:
          $ref: '#/definitions/AdotanteSchema'
    responses:
      200:
        description: Adotante atualizado com sucesso
        schema:
          $ref: '#/definitions/AdotanteSchema'
      400:
        description: Erro ao atualizar adotante
    """
    adotante_data = request.get_json()
    response = update_adotante_service(adotante_id, adotante_data)

    if response["status"] == 200:
        return jsonify(response["data"])

    return jsonify({"message": response["message"]}), response["status"]
