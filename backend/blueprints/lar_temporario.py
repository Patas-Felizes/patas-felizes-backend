from flask import Blueprint, request, jsonify
from backend.services.lar_temporario_service import (
    list_lar_temporarios_service,
    get_lar_temporario_service,
    create_lar_temporario_service,
    delete_lar_temporario_service,
    update_lar_temporario_service
)

lar_temporario_bp = Blueprint("lar_temporario", __name__, url_prefix="/temporary_shelters")

@lar_temporario_bp.route("/", methods=["GET"])
def list_lar_temporarios():
    """
    Lista todos os lares temporários armazenados no banco de dados.
    ---
    tags:
      - Lar Temporário
    definitions:
      LarTemporarioSchema:
        type: object
        properties:
          lar_temporario_id:
            type: integer
          animal_id:
            type: integer
          hospedeiro_id:
            type: integer
          periodo:
            type: string
          data_hospedagem:
            type: string
          data_cadastro:
            type: string
    responses:
        200:
            description: Lista de lares temporários
            schema:
              type: array
              items:
                $ref: '#/definitions/LarTemporarioSchema'
        404:
            description: Nenhum lar temporário encontrado no banco de dados.
    """
    response = list_lar_temporarios_service()

    if response["status"] == 200:
        return jsonify(response["data"])

    return jsonify({"message": response["message"]}), response["status"]


@lar_temporario_bp.route("/<int:lar_temporario_id>", methods=["GET"])
def get_lar_temporario(lar_temporario_id):
    """
    Retorna um lar temporário específico do banco de dados.
    ---
    tags:
      - Lar Temporário
    parameters:
      - in: path
        name: lar_temporario_id
        type: integer
        required: true
    definitions:
      LarTemporarioSchema:
        type: object
        properties:
          lar_temporario_id:
            type: integer
          animal_id:
            type: integer
          hospedeiro_id:
            type: integer
          periodo:
            type: string
          data_hospedagem:
            type: string
          data_cadastro:
            type: string
    responses:
        200:
            description: Lar temporário encontrado
            schema:
              $ref: '#/definitions/LarTemporarioSchema'
        404:
            description: Lar temporário não encontrado
    """
    response = get_lar_temporario_service(lar_temporario_id)

    if response["status"] == 200:
        return jsonify(response["data"])

    return jsonify({"message": response["message"]}), response["status"]


@lar_temporario_bp.route("/", methods=["POST"])
def create_lar_temporario():
    """
    Cria um novo registro de lar temporário no banco de dados.
    ---
    tags:
      - Lar Temporário
    parameters:
      - in: body
        name: lar_temporario
        schema:
          $ref: '#/definitions/LarTemporarioSchema'
    responses:
      201:
        description: Lar temporário criado com sucesso
        schema:
          $ref: '#/definitions/LarTemporarioSchema'
      400:
        description: Erro de validação ou ao criar o registro
    """
    lar_temporario_data = request.get_json()
    response = create_lar_temporario_service(lar_temporario_data)

    if response["status"] == 201:
        return jsonify(response["data"]), response["status"]

    return jsonify({"message": response["message"]}), response["status"]


@lar_temporario_bp.route("/<int:lar_temporario_id>", methods=["PUT"])
def update_lar_temporario(lar_temporario_id):
    """
    Atualiza um lar temporário específico no banco de dados.
    ---
    tags:
      - Lar Temporário
    parameters:
      - in: path
        name: lar_temporario_id
        type: integer
        required: true
      - in: body
        name: lar_temporario
        schema:
          $ref: '#/definitions/LarTemporarioSchema'
    responses:
      200:
        description: Lar temporário atualizado com sucesso
        schema:
          $ref: '#/definitions/LarTemporarioSchema'
      400:
        description: Erro de validação ou ao atualizar
    """
    lar_temporario_data = request.get_json()
    response = update_lar_temporario_service(lar_temporario_id, lar_temporario_data)

    if response["status"] == 200:
        return jsonify(response["data"])

    return jsonify({"message": response["message"]}), response["status"]


@lar_temporario_bp.route("/<int:lar_temporario_id>", methods=["DELETE"])
def delete_lar_temporario(lar_temporario_id):
    """
    Deleta um lar temporário específico do banco de dados.
    ---
    tags:
      - Lar Temporário
    parameters:
      - in: path
        name: lar_temporario_id
        type: integer
        required: true
    responses:
      204:
        description: Lar temporário deletado com sucesso
      404:
        description: Lar temporário não encontrado
    """
    response = delete_lar_temporario_service(lar_temporario_id)
    return jsonify({"message": response["message"]}), response["status"]
