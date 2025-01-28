from flask import Blueprint, request, jsonify
from backend.services.animal_service import list_animals_service, get_animal_service
from backend.services.animal_service import create_animal_service, delete_animal_service, update_animal_service
from backend.utils.decorators import jwt_required

animal_bp = Blueprint("animal", __name__, url_prefix="/animals")

@animal_bp.route("/", methods=["GET"])
# @jwt_required
def list_animals():
    """
    Lista todos os animais armazenados no banco de dados.
    ---
    tags:
      - Animais
    definitions:
      AnimalSchema:
        type: object
        properties:
          animal_id:
            type: integer
          nome:
            type: string
          idade:
            type: string
          foto:
            type: string
          descricao:
            type: string
          sexo:
            type: string
          castracao:
            type: string
          status:
            type: string
          especie:
            type: string
          data_cadastro:
            type: string
    responses:
        200:
            description: Lista de animais
            schema:
            type: array
            items:
                $ref: '#/definitions/AnimalSchema'
        404:
            description: Nenhum animal encontrado no banco de dados.
    """
    # page = request.args.get("page", 1, type=int)
    # per_page = request.args.get("per_page", 10, type=int)

    response = list_animals_service()

    if response["status"] == 200:
        return jsonify(response["data"])

    return jsonify({"message": response["message"]}), response["status"]

@animal_bp.route("/<int:animal_id>", methods=["GET"])
def get_animal(animal_id):
    """
    Retorna um animal específico do banco de dados.
    ---
    tags:
      - Animais
    parameters:
      - in: path
        name: animal_id
        type: integer
        required: true
    definitions:
      AnimalSchema:
        type: object
        properties:
          animal_id:
            type: integer
          nome:
            type: string
          idade:
            type: string
          foto:
            type: string
          descricao:
            type: string
          sexo:
            type: string
          castracao:
            type: string
          status:
            type: string
          especie:
            type: string
          data_cadastro:
            type: string
    responses:
        200:
            description: Animal encontrado
            schema:
                $ref: '#/definitions/AnimalSchema'
        404:
            description: Animal não encontrado
    """
    response = get_animal_service(animal_id)

    if response["status"] == 200:
        return jsonify(response["data"])

    return jsonify({"message": response["message"]}), response["status"]

@animal_bp.route("/", methods=["POST"])
def create_animal():
    """
    Cria um novo animal no banco de dados.
    ---
    tags:
      - Animais
    parameters:
      - in: body
        name: animal
        schema:
          $ref: '#/definitions/AnimalSchema'
    responses:
      201:
        description: Animal criado com sucesso
        schema:
          $ref: '#/definitions/AnimalSchema'
      400:
        description: Erro ao criar animal
    """
    animal_data = request.get_json()

    response = create_animal_service(animal_data)

    if response["status"] == 201:
        return jsonify(response["data"]), response["status"]

    return jsonify({"message": response["message"]}), response["status"]

@animal_bp.route("/<int:animal_id>", methods=["DELETE"])
def delete_animal(animal_id):
    """
    Deleta um animal específico do banco de dados.
    ---
    tags:
      - Animais
    parameters:
      - in: path
        name: animal_id
        type: integer
        required: true
    responses:
      204:
        description: Animal deletado com sucesso
      404:
        description: Animal não encontrado
    """
    response = delete_animal_service(animal_id)

    return jsonify({"message": response["message"]}), response["status"]

@animal_bp.route("/<int:animal_id>", methods=["PUT"])
def update_animal(animal_id):
    """
    Atualiza um animal específico do banco de dados.
    ---
    tags:
      - Animais
    parameters:
      - in: path
        name: animal_id
        type: integer
        required: true
      - in: body
        name: animal
        schema:
          $ref: '#/definitions/AnimalSchema'
    responses:
      200:
        description: Animal atualizado com sucesso
        schema:
          $ref: '#/definitions/AnimalSchema'
      400:
        description: Erro ao atualizar animal
    """
    animal_data = request.get_json()

    response = update_animal_service(animal_id, animal_data)

    if response["status"] == 200:
        return jsonify(response["data"])

    return jsonify({"message": response["message"]}), response["status"]