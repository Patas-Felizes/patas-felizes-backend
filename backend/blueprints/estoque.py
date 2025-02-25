from flask import Blueprint, request, jsonify
from backend.services.estoque_service import list_estoque_service, get_estoque_service
from backend.services.estoque_service import create_estoque_service, delete_estoque_service, update_estoque_service

estoque_bp = Blueprint("estoque", __name__, url_prefix="/estoque")

@estoque_bp.route("/", methods=["GET"])
def list_estoque():
    """
    Lista todos os itens de estoque armazenados no banco de dados.
    ---
    tags:
      - Estoque
    definitions:
      EstoqueSchema:
        type: object
        properties:
          estoque_id:
            type: integer
          categoria:
            type: string
          tipo_item:
            type: string
          descricao:
            type: string
          especie_animal:
            type: string
          quantidade:
            type: string
    responses:
        200:
            description: Lista de itens no estoque
            schema:
            type: array
            items:
                $ref: '#/definitions/EstoqueSchema'
        404:
            description: Nenhum item encontrado no estoque.
    """
    response = list_estoque_service()

    if response["status"] == 200:
        return jsonify(response["data"])

    return jsonify({"message": response["message"]}), response["status"]

@estoque_bp.route("/<int:estoque_id>", methods=["GET"])
def get_estoque(estoque_id):
    """
    Retorna um item específico do estoque.
    ---
    tags:
      - Estoque
    parameters:
      - in: path
        name: estoque_id
        type: integer
        required: true
    definitions:
      EstoqueSchema:
        type: object
        properties:
          estoque_id:
            type: integer
          categoria:
            type: string
          tipo_item:
            type: string
          descricao:
            type: string
          especie_animal:
            type: string
          quantidade:
            type: string
    responses:
        200:
            description: Item encontrado
            schema:
                $ref: '#/definitions/EstoqueSchema'
        404:
            description: Item não encontrado no estoque.
    """
    response = get_estoque_service(estoque_id)

    if response["status"] == 200:
        return jsonify(response["data"])

    return jsonify({"message": response["message"]}), response["status"]

@estoque_bp.route("/", methods=["POST"])
def create_estoque():
    """
    Cria um novo item no estoque.
    ---
    tags:
      - Estoque
    parameters:
      - in: body
        name: estoque
        schema:
          $ref: '#/definitions/EstoqueSchema'
    responses:
      201:
        description: Item criado com sucesso
        schema:
          $ref: '#/definitions/EstoqueSchema'
      400:
        description: Erro ao criar item no estoque.
    """
    estoque_data = request.get_json()

    response = create_estoque_service(estoque_data)

    if response["status"] == 201:
        return jsonify(response["data"]), response["status"]

    return jsonify({"message": response["message"]}), response["status"]

@estoque_bp.route("/<int:estoque_id>", methods=["PUT"])
def update_estoque(estoque_id):
    """
    Atualiza um item específico do estoque.
    ---
    tags:
      - Estoque
    parameters:
      - in: path
        name: estoque_id
        type: integer
        required: true
      - in: body
        name: estoque
        schema:
          $ref: '#/definitions/EstoqueSchema'
    responses:
      200:
        description: Item atualizado com sucesso
        schema:
          $ref: '#/definitions/EstoqueSchema'
      400:
        description: Erro ao atualizar item no estoque.
    """
    estoque_data = request.get_json()

    response = update_estoque_service(estoque_id, estoque_data)

    if response["status"] == 200:
        return jsonify(response["data"])

    return jsonify({"message": response["message"]}), response["status"]

@estoque_bp.route("/<int:estoque_id>", methods=["DELETE"])
def delete_estoque(estoque_id):
    """
    Deleta um item específico do estoque.
    ---
    tags:
      - Estoque
    parameters:
      - in: path
        name: estoque_id
        type: integer
        required: true
    responses:
      204:
        description: Item deletado com sucesso
      404:
        description: Item não encontrado no estoque.
    """
    response = delete_estoque_service(estoque_id)

    return jsonify({"message": response["message"]}), response["status"]
