from flask import Blueprint, request, jsonify
from backend.services.doacao_service import list_doacoes_service, get_doacao_service
from backend.services.doacao_service import create_doacao_service, delete_doacao_service, update_doacao_service

doacao_bp = Blueprint("doacao", __name__, url_prefix="/doacoes")

@doacao_bp.route("/", methods=["GET"])
def list_doacoes():
    """
    Lista todas as doações armazenadas no banco de dados.
    ---
    tags:
      - Doações
    definitions:
      DoacaoSchema:
        type: object
        properties:
          doacao_id:
            type: integer
          doador:
            type: string
          valor:
            type: string
          data_doacao:
            type: string
          animal_id:
            type: integer
          companha_id:
            type: integer
          comprovante:
            type: string
    responses:
        200:
            description: Lista de doações
            schema:
            type: array
            items:
                $ref: '#/definitions/DoacaoSchema'
        404:
            description: Nenhuma doação encontrada no banco de dados.
    """
    response = list_doacoes_service()

    if response["status"] == 200:
        return jsonify(response["data"])

    return jsonify({"message": response["message"]}), response["status"]

@doacao_bp.route("/<int:doacao_id>", methods=["GET"])
def get_doacao(doacao_id):
    """
    Retorna uma doação específica do banco de dados.
    ---
    tags:
      - Doações
    parameters:
      - in: path
        name: doacao_id
        type: integer
        required: true
    definitions:
      DoacaoSchema:
        type: object
        properties:
          doacao_id:
            type: integer
          doador:
            type: string
          valor:
            type: string
          data_doacao:
            type: string
          animal_id:
            type: integer
          companha_id:
            type: integer
          comprovante:
            type: string
    responses:
        200:
            description: Doação encontrada
            schema:
                $ref: '#/definitions/DoacaoSchema'
        404:
            description: Doação não encontrada
    """
    response = get_doacao_service(doacao_id)

    if response["status"] == 200:
        return jsonify(response["data"])

    return jsonify({"message": response["message"]}), response["status"]

@doacao_bp.route("/", methods=["POST"])
def create_doacao():
    """
    Cria uma nova doação no banco de dados.
    ---
    tags:
      - Doações
    parameters:
      - in: body
        name: doacao
        schema:
          $ref: '#/definitions/DoacaoSchema'
    responses:
      201:
        description: Doação criada com sucesso
        schema:
          $ref: '#/definitions/DoacaoSchema'
      400:
        description: Erro ao criar doação
    """
    doacao_data = request.get_json()

    response = create_doacao_service(doacao_data)

    if response["status"] == 201:
        return jsonify(response["data"]), response["status"]

    return jsonify({"message": response["message"]}), response["status"]

@doacao_bp.route("/<int:doacao_id>", methods=["DELETE"])
def delete_doacao(doacao_id):
    """
    Deleta uma doação específica do banco de dados.
    ---
    tags:
      - Doações
    parameters:
      - in: path
        name: doacao_id
        type: integer
        required: true
    responses:
      204:
        description: Doação deletada com sucesso
      404:
        description: Doação não encontrada
    """
    response = delete_doacao_service(doacao_id)

    return jsonify({"message": response["message"]}), response["status"]

@doacao_bp.route("/<int:doacao_id>", methods=["PUT"])
def update_doacao(doacao_id):
    """
    Atualiza uma doação específica do banco de dados.
    ---
    tags:
      - Doações
    parameters:
      - in: path
        name: doacao_id
        type: integer
        required: true
      - in: body
        name: doacao
        schema:
          $ref: '#/definitions/DoacaoSchema'
    responses:
      200:
        description: Doação atualizada com sucesso
        schema:
          $ref: '#/definitions/DoacaoSchema'
      400:
        description: Erro ao atualizar doação
    """
    doacao_data = request.get_json()

    response = update_doacao_service(doacao_id, doacao_data)

    if response["status"] == 200:
        return jsonify(response["data"])

    return jsonify({"message": response["message"]}), response["status"]
