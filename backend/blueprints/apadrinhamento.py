from flask import Blueprint, request, jsonify
from backend.services.apadrinhamento_service import (
    list_apadrinhamentos_service,
    get_apadrinhamento_service,
    create_apadrinhamento_service,
    update_apadrinhamento_service,
    delete_apadrinhamento_service,
)

apadrinhamento_bp = Blueprint("apadrinhamento", __name__, url_prefix="/apadrinhamentos")


@apadrinhamento_bp.route("/", methods=["GET"])
def list_apadrinhamentos():
    """
    Lista todos os apadrinhamentos armazenados no banco de dados.
    ---
    tags:
      - Apadrinhamentos
    definitions:
      ApadrinhamentoSchema:
        type: object
        properties:
          apadrinhamento_id:
            type: integer
          animal_id:
            type: integer
          nome_apadrinhador:
            type: string
          valor:
            type: string
          regularidade:
            type: string
    responses:
      200:
        description: Lista de apadrinhamentos
        schema:
          type: array
          items:
            $ref: '#/definitions/ApadrinhamentoSchema'
      404:
        description: Nenhum apadrinhamento encontrado
    """
    response = list_apadrinhamentos_service()

    if response["status"] == 200:
        return jsonify(response["data"])

    return jsonify({"message": response["message"]}), response["status"]


@apadrinhamento_bp.route("/<int:apadrinhamento_id>", methods=["GET"])
def get_apadrinhamento(apadrinhamento_id):
    """
    Retorna um apadrinhamento específico do banco de dados.
    ---
    tags:
      - Apadrinhamentos
    parameters:
      - in: path
        name: apadrinhamento_id
        type: integer
        required: true
    definitions:
      ApadrinhamentoSchema:
        type: object
        properties:
          apadrinhamento_id:
            type: integer
          animal_id:
            type: integer
          nome_apadrinhador:
            type: string
          valor:
            type: string
          regularidade:
            type: string
    responses:
      200:
        description: Apadrinhamento encontrado
        schema:
          $ref: '#/definitions/ApadrinhamentoSchema'
      404:
        description: Apadrinhamento não encontrado
    """
    response = get_apadrinhamento_service(apadrinhamento_id)

    if response["status"] == 200:
        return jsonify(response["data"])

    return jsonify({"message": response["message"]}), response["status"]


@apadrinhamento_bp.route("/", methods=["POST"])
def create_apadrinhamento():
    """
    Cria um novo apadrinhamento no banco de dados.
    ---
    tags:
      - Apadrinhamentos
    parameters:
      - in: body
        name: apadrinhamento
        schema:
          $ref: '#/definitions/ApadrinhamentoSchema'
    responses:
      201:
        description: Apadrinhamento criado com sucesso
        schema:
          $ref: '#/definitions/ApadrinhamentoSchema'
      400:
        description: Erro de validação ou de request
    """
    apadrinhamento_data = request.get_json()

    response = create_apadrinhamento_service(apadrinhamento_data)

    if response["status"] == 201:
        return jsonify(response["data"]), response["status"]

    return jsonify({"message": response["message"]}), response["status"]


@apadrinhamento_bp.route("/<int:apadrinhamento_id>", methods=["PUT"])
def update_apadrinhamento(apadrinhamento_id):
    """
    Atualiza um apadrinhamento específico no banco de dados.
    ---
    tags:
      - Apadrinhamentos
    parameters:
      - in: path
        name: apadrinhamento_id
        type: integer
        required: true
      - in: body
        name: apadrinhamento
        schema:
          $ref: '#/definitions/ApadrinhamentoSchema'
    responses:
      200:
        description: Apadrinhamento atualizado com sucesso
        schema:
          $ref: '#/definitions/ApadrinhamentoSchema'
      400:
        description: Erro de validação ou de request
      404:
        description: Apadrinhamento não encontrado
    """
    apadrinhamento_data = request.get_json()

    response = update_apadrinhamento_service(apadrinhamento_id, apadrinhamento_data)

    if response["status"] == 200:
        return jsonify(response["data"])

    return jsonify({"message": response["message"]}), response["status"]


@apadrinhamento_bp.route("/<int:apadrinhamento_id>", methods=["DELETE"])
def delete_apadrinhamento(apadrinhamento_id):
    """
    Deleta um apadrinhamento específico do banco de dados.
    ---
    tags:
      - Apadrinhamentos
    parameters:
      - in: path
        name: apadrinhamento_id
        type: integer
        required: true
    responses:
      204:
        description: Apadrinhamento deletado com sucesso
      404:
        description: Apadrinhamento não encontrado
    """
    response = delete_apadrinhamento_service(apadrinhamento_id)
    return jsonify({"message": response["message"]}), response["status"]
