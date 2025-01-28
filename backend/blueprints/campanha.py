from flask import Blueprint, request, jsonify
from backend.services.campanha_service import (
    list_campanhas_service,
    get_campanha_service,
    create_campanha_service,
    delete_campanha_service,
    update_campanha_service,
)

campanha_bp = Blueprint("campanha", __name__, url_prefix="/campanhas")

@campanha_bp.route("/", methods=["GET"])
def list_campanhas():
    """
    Lista todas as campanhas armazenadas no banco de dados.
    ---
    tags:
      - Campanhas
    definitions:
      CampanhaSchema:
        type: object
        properties:
          campanha_id:
            type: integer
          nome:
            type: string
          tipo:
            type: string
          data_inicio:
            type: string
          data_termino:
            type: string
          descricao:
            type: string
          local:
            type: string
    responses:
      200:
        description: Lista de campanhas
        schema:
          type: array
          items:
            $ref: '#/definitions/CampanhaSchema'
      404:
        description: Nenhuma campanha encontrada no banco de dados.
    """
    response = list_campanhas_service()
    if response["status"] == 200:
        return jsonify(response["data"])
    return jsonify({"message": response["message"]}), response["status"]


@campanha_bp.route("/<int:campanha_id>", methods=["GET"])
def get_campanha(campanha_id):
    """
    Retorna uma campanha específica do banco de dados.
    ---
    tags:
      - Campanhas
    parameters:
      - in: path
        name: campanha_id
        type: integer
        required: true
    definitions:
      CampanhaSchema:
        type: object
        properties:
          campanha_id:
            type: integer
          nome:
            type: string
          tipo:
            type: string
          data_inicio:
            type: string
          data_termino:
            type: string
          descricao:
            type: string
          local:
            type: string
    responses:
      200:
        description: Campanha encontrada
        schema:
          $ref: '#/definitions/CampanhaSchema'
      404:
        description: Campanha não encontrada
    """
    response = get_campanha_service(campanha_id)
    if response["status"] == 200:
        return jsonify(response["data"])
    return jsonify({"message": response["message"]}), response["status"]


@campanha_bp.route("/", methods=["POST"])
def create_campanha():
    """
    Cria uma nova campanha no banco de dados.
    ---
    tags:
      - Campanhas
    parameters:
      - in: body
        name: campanha
        schema:
          $ref: '#/definitions/CampanhaSchema'
    responses:
      201:
        description: Campanha criada com sucesso
        schema:
          $ref: '#/definitions/CampanhaSchema'
      400:
        description: Erro ao criar campanha
    """
    campanha_data = request.get_json()
    response = create_campanha_service(campanha_data)

    if response["status"] == 201:
        return jsonify(response["data"]), response["status"]

    return jsonify({"message": response["message"]}), response["status"]


@campanha_bp.route("/<int:campanha_id>", methods=["DELETE"])
def delete_campanha(campanha_id):
    """
    Deleta uma campanha específica do banco de dados.
    ---
    tags:
      - Campanhas
    parameters:
      - in: path
        name: campanha_id
        type: integer
        required: true
    responses:
      204:
        description: Campanha deletada com sucesso
      404:
        description: Campanha não encontrada
    """
    response = delete_campanha_service(campanha_id)
    return jsonify({"message": response["message"]}), response["status"]


@campanha_bp.route("/<int:campanha_id>", methods=["PUT"])
def update_campanha(campanha_id):
    """
    Atualiza uma campanha específica do banco de dados.
    ---
    tags:
      - Campanhas
    parameters:
      - in: path
        name: campanha_id
        type: integer
        required: true
      - in: body
        name: campanha
        schema:
          $ref: '#/definitions/CampanhaSchema'
    responses:
      200:
        description: Campanha atualizada com sucesso
        schema:
          $ref: '#/definitions/CampanhaSchema'
      400:
        description: Erro ao atualizar campanha
    """
    campanha_data = request.get_json()
    response = update_campanha_service(campanha_id, campanha_data)

    if response["status"] == 200:
        return jsonify(response["data"])
    return jsonify({"message": response["message"]}), response["status"]
