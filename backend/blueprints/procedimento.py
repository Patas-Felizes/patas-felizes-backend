from flask import Blueprint, request, jsonify
from backend.services.procedimento_service import (
    list_procedimentos_service,
    get_procedimento_service,
    create_procedimento_service,
    update_procedimento_service,
    delete_procedimento_service
)

procedimento_bp = Blueprint("procedimento", __name__, url_prefix="/procedimentos")

@procedimento_bp.route("/", methods=["GET"])
def list_procedimentos():
    """
    Lista todos os procedimentos armazenados no banco de dados.
    ---
    tags:
      - Procedimentos
    definitions:
      ProcedimentoSchema:
        type: object
        properties:
          procedimento_id:
            type: integer
          tipo:
            type: string
          descricao:
            type: string
          valor:
            type: string
          data_procedimento:
            type: string
          animal_id:
            type: integer
          voluntario_id:
            type: integer
          despesa_id:
            type: integer
    responses:
      200:
        description: Lista de procedimentos
        schema:
          type: array
          items:
            $ref: '#/definitions/ProcedimentoSchema'
      404:
        description: Nenhum procedimento encontrado no banco de dados.
    """
    response = list_procedimentos_service()

    if response["status"] == 200:
        return jsonify(response["data"]), response["status"]

    return jsonify({"message": response["message"]}), response["status"]


@procedimento_bp.route("/<int:procedimento_id>", methods=["GET"])
def get_procedimento(procedimento_id):
    """
    Retorna um procedimento específico do banco de dados.
    ---
    tags:
      - Procedimentos
    parameters:
      - in: path
        name: procedimento_id
        type: integer
        required: true
    definitions:
      ProcedimentoSchema:
        type: object
        properties:
          procedimento_id:
            type: integer
          tipo:
            type: string
          descricao:
            type: string
          valor:
            type: string
          data_procedimento:
            type: string
          animal_id:
            type: integer
          voluntario_id:
            type: integer
          despesa_id:
            type: integer
    responses:
      200:
        description: Procedimento encontrado
        schema:
          $ref: '#/definitions/ProcedimentoSchema'
      404:
        description: Procedimento não encontrado
    """
    response = get_procedimento_service(procedimento_id)

    if response["status"] == 200:
        return jsonify(response["data"]), response["status"]

    return jsonify({"message": response["message"]}), response["status"]


@procedimento_bp.route("/", methods=["POST"])
def create_procedimento():
    """
    Cria um novo procedimento no banco de dados.
    ---
    tags:
      - Procedimentos
    parameters:
      - in: body
        name: procedimento
        schema:
          $ref: '#/definitions/ProcedimentoSchema'
    responses:
      201:
        description: Procedimento criado com sucesso
        schema:
          $ref: '#/definitions/ProcedimentoSchema'
      400:
        description: Erro ao criar procedimento
    """
    data = request.get_json()
    response = create_procedimento_service(data)

    if response["status"] == 201:
        return jsonify(response["data"]), response["status"]

    return jsonify({"message": response["message"]}), response["status"]


@procedimento_bp.route("/<int:procedimento_id>", methods=["PUT"])
def update_procedimento(procedimento_id):
    """
    Atualiza um procedimento específico do banco de dados.
    ---
    tags:
      - Procedimentos
    parameters:
      - in: path
        name: procedimento_id
        type: integer
        required: true
      - in: body
        name: procedimento
        schema:
          $ref: '#/definitions/ProcedimentoSchema'
    responses:
      200:
        description: Procedimento atualizado com sucesso
        schema:
          $ref: '#/definitions/ProcedimentoSchema'
      400:
        description: Erro ao atualizar procedimento
    """
    data = request.get_json()
    response = update_procedimento_service(procedimento_id, data)

    if response["status"] == 200:
        return jsonify(response["data"]), response["status"]

    return jsonify({"message": response["message"]}), response["status"]


@procedimento_bp.route("/<int:procedimento_id>", methods=["DELETE"])
def delete_procedimento(procedimento_id):
    """
    Deleta um procedimento específico do banco de dados.
    ---
    tags:
      - Procedimentos
    parameters:
      - in: path
        name: procedimento_id
        type: integer
        required: true
    responses:
      204:
        description: Procedimento deletado com sucesso
      404:
        description: Procedimento não encontrado
    """
    response = delete_procedimento_service(procedimento_id)

    return jsonify({"message": response["message"]}), response["status"]
