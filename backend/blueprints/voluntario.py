from flask import Blueprint, request, jsonify
from backend.services.voluntario_service import (
    list_voluntarios_service,
    get_voluntario_service,
    create_voluntario_service,
    delete_voluntario_service,
    update_voluntario_service,
)

voluntario_bp = Blueprint("voluntario", __name__, url_prefix="/voluntarios")


@voluntario_bp.route("/", methods=["GET"])
def list_voluntarios():
    """
    Lista todos os voluntários armazenados no banco de dados.
    ---
    tags:
      - Voluntários
    definitions:
      VoluntarioSchema:
        type: object
        properties:
          voluntario_id:
            type: integer
          nome:
            type: string
          foto:
            type: string
          email:
            type: string
          telefone:
            type: string
    responses:
        200:
            description: Lista de voluntários
            schema:
              type: array
              items:
                $ref: '#/definitions/VoluntarioSchema'
        404:
            description: Nenhum voluntário encontrado no banco de dados.
    """
    response = list_voluntarios_service()

    if response["status"] == 200:
        return jsonify(response["data"])

    return jsonify({"message": response["message"]}), response["status"]


@voluntario_bp.route("/<int:voluntario_id>", methods=["GET"])
def get_voluntario(voluntario_id):
    """
    Retorna um voluntário específico do banco de dados.
    ---
    tags:
      - Voluntários
    parameters:
      - in: path
        name: voluntario_id
        type: integer
        required: true
    definitions:
      VoluntarioSchema:
        type: object
        properties:
          voluntario_id:
            type: integer
          nome:
            type: string
          foto:
            type: string
          email:
            type: string
          telefone:
            type: string
    responses:
        200:
            description: Voluntário encontrado
            schema:
              $ref: '#/definitions/VoluntarioSchema'
        404:
            description: Voluntário não encontrado
    """
    response = get_voluntario_service(voluntario_id)

    if response["status"] == 200:
        return jsonify(response["data"])

    return jsonify({"message": response["message"]}), response["status"]


@voluntario_bp.route("/", methods=["POST"])
def create_voluntario():
    """
    Cria um novo voluntário no banco de dados.
    ---
    tags:
      - Voluntários
    parameters:
      - in: body
        name: voluntario
        schema:
          $ref: '#/definitions/VoluntarioSchema'
    responses:
      201:
        description: Voluntário criado com sucesso
        schema:
          $ref: '#/definitions/VoluntarioSchema'
      400:
        description: Erro ao criar voluntário
    """
    voluntario_data = request.get_json()

    response = create_voluntario_service(voluntario_data)

    if response["status"] == 201:
        return jsonify(response["data"]), response["status"]

    return jsonify({"message": response["message"]}), response["status"]


@voluntario_bp.route("/<int:voluntario_id>", methods=["DELETE"])
def delete_voluntario(voluntario_id):
    """
    Deleta um voluntário específico do banco de dados.
    ---
    tags:
      - Voluntários
    parameters:
      - in: path
        name: voluntario_id
        type: integer
        required: true
    responses:
      204:
        description: Voluntário deletado com sucesso
      404:
        description: Voluntário não encontrado
    """
    response = delete_voluntario_service(voluntario_id)

    return jsonify({"message": response["message"]}), response["status"]


@voluntario_bp.route("/<int:voluntario_id>", methods=["PUT"])
def update_voluntario(voluntario_id):
    """
    Atualiza um voluntário específico do banco de dados.
    ---
    tags:
      - Voluntários
    parameters:
      - in: path
        name: voluntario_id
        type: integer
        required: true
      - in: body
        name: voluntario
        schema:
          $ref: '#/definitions/VoluntarioSchema'
    responses:
      200:
        description: Voluntário atualizado com sucesso
        schema:
          $ref: '#/definitions/VoluntarioSchema'
      400:
        description: Erro ao atualizar voluntário
    """
    voluntario_data = request.get_json()

    response = update_voluntario_service(voluntario_id, voluntario_data)

    if response["status"] == 200:
        return jsonify(response["data"])

    return jsonify({"message": response["message"]}), response["status"]
