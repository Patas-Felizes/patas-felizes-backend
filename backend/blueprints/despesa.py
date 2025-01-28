from flask import Blueprint, request, jsonify
from backend.services.despesa_service import (
    list_despesas_service,
    get_despesa_service,
    create_despesa_service,
    delete_despesa_service,
    update_despesa_service,
)

despesa_bp = Blueprint("despesa", __name__, url_prefix="/despesas")


@despesa_bp.route("/", methods=["GET"])
def list_despesas():
    """
    Lista todas as despesas armazenadas no banco de dados.
    ---
    tags:
      - Despesas
    definitions:
      DespesaSchema:
        type: object
        properties:
          despesa_id:
            type: integer
          valor:
            type: string
          data_despesa:
            type: string
          tipo:
            type: string
          animal_id:
            type: integer
          procedimento_id:
            type: integer
          comprovante:
            type: string
    responses:
        200:
            description: Lista de despesas
            schema:
            type: array
            items:
                $ref: '#/definitions/DespesaSchema'
        404:
            description: Nenhuma despesa encontrada no banco de dados.
    """
    response = list_despesas_service()

    if response["status"] == 200:
        return jsonify(response["data"])

    return jsonify({"message": response["message"]}), response["status"]


@despesa_bp.route("/<int:despesa_id>", methods=["GET"])
def get_despesa(despesa_id):
    """
    Retorna uma despesa específica do banco de dados.
    ---
    tags:
      - Despesas
    parameters:
      - in: path
        name: despesa_id
        type: integer
        required: true
    definitions:
      DespesaSchema:
        type: object
        properties:
          despesa_id:
            type: integer
          valor:
            type: string
          data_despesa:
            type: string
          tipo:
            type: string
          animal_id:
            type: integer
          procedimento_id:
            type: integer
          comprovante:
            type: string
    responses:
        200:
            description: Despesa encontrada
            schema:
                $ref: '#/definitions/DespesaSchema'
        404:
            description: Despesa não encontrada
    """
    response = get_despesa_service(despesa_id)

    if response["status"] == 200:
        return jsonify(response["data"])

    return jsonify({"message": response["message"]}), response["status"]


@despesa_bp.route("/", methods=["POST"])
def create_despesa():
    """
    Cria uma nova despesa no banco de dados.
    ---
    tags:
      - Despesas
    parameters:
      - in: body
        name: despesa
        schema:
          $ref: '#/definitions/DespesaSchema'
    responses:
      201:
        description: Despesa criada com sucesso
        schema:
          $ref: '#/definitions/DespesaSchema'
      400:
        description: Erro ao criar despesa
    """
    despesa_data = request.get_json()

    response = create_despesa_service(despesa_data)

    if response["status"] == 201:
        return jsonify(response["data"]), response["status"]

    return jsonify({"message": response["message"]}), response["status"]


@despesa_bp.route("/<int:despesa_id>", methods=["DELETE"])
def delete_despesa(despesa_id):
    """
    Deleta uma despesa específica do banco de dados.
    ---
    tags:
      - Despesas
    parameters:
      - in: path
        name: despesa_id
        type: integer
        required: true
    responses:
      204:
        description: Despesa deletada com sucesso
      404:
        description: Despesa não encontrada
    """
    response = delete_despesa_service(despesa_id)

    return jsonify({"message": response["message"]}), response["status"]


@despesa_bp.route("/<int:despesa_id>", methods=["PUT"])
def update_despesa(despesa_id):
    """
    Atualiza uma despesa específica do banco de dados.
    ---
    tags:
      - Despesas
    parameters:
      - in: path
        name: despesa_id
        type: integer
        required: true
      - in: body
        name: despesa
        schema:
          $ref: '#/definitions/DespesaSchema'
    responses:
      200:
        description: Despesa atualizada com sucesso
        schema:
          $ref: '#/definitions/DespesaSchema'
      400:
        description: Erro ao atualizar despesa
    """
    despesa_data = request.get_json()

    response = update_despesa_service(despesa_id, despesa_data)

    if response["status"] == 200:
        return jsonify(response["data"])

    return jsonify({"message": response["message"]}), response["status"]
