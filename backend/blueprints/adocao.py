from flask import Blueprint, request, jsonify
from backend.services.adocao_service import (
    list_adocoes_service,
    get_adocao_service,
    create_adocao_service,
    delete_adocao_service,
    update_adocao_service
)

adocao_bp = Blueprint("adocao", __name__, url_prefix="/adocoes")

@adocao_bp.route("/", methods=["GET"])
def list_adocoes():
    """
    Lista todas as adoções armazenadas no banco de dados.
    ---
    tags:
      - Adoções
    definitions:
      AdocaoSchema:
        type: object
        properties:
          adocao_id:
            type: integer
          animal_id:
            type: integer
          adotante_id:
            type: integer
          companha_id:
            type: integer
          data_devolucao:
            type: string
          motivo_devolucao:
            type: string
          data_adocao:
            type: string
          data_cadastro:
            type: string
    responses:
      200:
        description: Lista de adoções
        schema:
          type: array
          items:
            $ref: '#/definitions/AdocaoSchema'
      404:
        description: Nenhuma adoção encontrada no banco de dados.
    """
    response = list_adocoes_service()

    if response["status"] == 200:
        return jsonify(response["data"])

    return jsonify({"message": response["message"]}), response["status"]


@adocao_bp.route("/<int:adocao_id>", methods=["GET"])
def get_adocao(adocao_id):
    """
    Retorna uma adoção específica do banco de dados.
    ---
    tags:
      - Adoções
    parameters:
      - in: path
        name: adocao_id
        type: integer
        required: true
    definitions:
      AdocaoSchema:
        type: object
        properties:
          adocao_id:
            type: integer
          animal_id:
            type: integer
          adotante_id:
            type: integer
          companha_id:
            type: integer
          data_devolucao:
            type: string
          motivo_devolucao:
            type: string
          data_adocao:
            type: string
          data_cadastro:
            type: string
    responses:
      200:
        description: Adoção encontrada
        schema:
          $ref: '#/definitions/AdocaoSchema'
      404:
        description: Adoção não encontrada
    """
    response = get_adocao_service(adocao_id)

    if response["status"] == 200:
        return jsonify(response["data"])

    return jsonify({"message": response["message"]}), response["status"]


@adocao_bp.route("/", methods=["POST"])
def create_adocao():
    """
    Cria uma nova adoção no banco de dados.
    ---
    tags:
      - Adoções
    parameters:
      - in: body
        name: adocao
        schema:
          $ref: '#/definitions/AdocaoSchema'
    responses:
      201:
        description: Adoção criada com sucesso
        schema:
          $ref: '#/definitions/AdocaoSchema'
      400:
        description: Erro ao criar adoção
    """
    adocao_data = request.get_json()

    response = create_adocao_service(adocao_data)

    if response["status"] == 201:
        return jsonify(response["data"]), response["status"]

    return jsonify({"message": response["message"]}), response["status"]


@adocao_bp.route("/<int:adocao_id>", methods=["DELETE"])
def delete_adocao(adocao_id):
    """
    Deleta uma adoção específica do banco de dados.
    ---
    tags:
      - Adoções
    parameters:
      - in: path
        name: adocao_id
        type: integer
        required: true
    responses:
      204:
        description: Adoção deletada com sucesso
      404:
        description: Adoção não encontrada
    """
    response = delete_adocao_service(adocao_id)
    return jsonify({"message": response["message"]}), response["status"]


@adocao_bp.route("/<int:adocao_id>", methods=["PUT"])
def update_adocao(adocao_id):
    """
    Atualiza uma adoção específica no banco de dados.
    ---
    tags:
      - Adoções
    parameters:
      - in: path
        name: adocao_id
        type: integer
        required: true
      - in: body
        name: adocao
        schema:
          $ref: '#/definitions/AdocaoSchema'
    responses:
      200:
        description: Adoção atualizada com sucesso
        schema:
          $ref: '#/definitions/AdocaoSchema'
      400:
        description: Erro ao atualizar adoção
    """
    adocao_data = request.get_json()

    response = update_adocao_service(adocao_id, adocao_data)

    if response["status"] == 200:
        return jsonify(response["data"])

    return jsonify({"message": response["message"]}), response["status"]
