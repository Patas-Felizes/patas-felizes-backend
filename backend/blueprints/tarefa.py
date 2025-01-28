from flask import Blueprint, request, jsonify
from backend.services.tarefa_service import (
    list_tarefas_service,
    get_tarefa_service,
    create_tarefa_service,
    update_tarefa_service,
    delete_tarefa_service,
)

tarefa_bp = Blueprint("tarefa", __name__, url_prefix="/tarefas")

@tarefa_bp.route("/", methods=["GET"])
def list_tarefas():
    """
    Lista todas as tarefas armazenadas no banco de dados.
    ---
    tags:
      - Tarefas
    definitions:
      TarefaSchema:
        type: object
        properties:
          tarefa_id:
            type: integer
          tipo:
            type: string
          descricao:
            type: string
          data_tarefa:
            type: string
          voluntario_id:
            type: integer
          animal_id:
            type: integer
    responses:
        200:
            description: Lista de tarefas
            schema:
            type: array
            items:
                $ref: '#/definitions/TarefaSchema'
        404:
            description: Nenhuma tarefa encontrada no banco de dados.
    """
    response = list_tarefas_service()

    if response["status"] == 200:
        return jsonify(response["data"])

    return jsonify({"message": response["message"]}), response["status"]

@tarefa_bp.route("/<int:tarefa_id>", methods=["GET"])
def get_tarefa(tarefa_id):
    """
    Retorna uma tarefa específica do banco de dados.
    ---
    tags:
      - Tarefas
    parameters:
      - in: path
        name: tarefa_id
        type: integer
        required: true
    definitions:
      TarefaSchema:
        type: object
        properties:
          tarefa_id:
            type: integer
          tipo:
            type: string
          descricao:
            type: string
          data_tarefa:
            type: string
          voluntario_id:
            type: integer
          animal_id:
            type: integer
    responses:
        200:
            description: Tarefa encontrada
            schema:
                $ref: '#/definitions/TarefaSchema'
        404:
            description: Tarefa não encontrada
    """
    response = get_tarefa_service(tarefa_id)

    if response["status"] == 200:
        return jsonify(response["data"])

    return jsonify({"message": response["message"]}), response["status"]

@tarefa_bp.route("/", methods=["POST"])
def create_tarefa():
    """
    Cria uma nova tarefa no banco de dados.
    ---
    tags:
      - Tarefas
    parameters:
      - in: body
        name: tarefa
        schema:
          $ref: '#/definitions/TarefaSchema'
    responses:
      201:
        description: Tarefa criada com sucesso
        schema:
          $ref: '#/definitions/TarefaSchema'
      400:
        description: Erro ao criar tarefa
    """
    tarefa_data = request.get_json()

    response = create_tarefa_service(tarefa_data)

    if response["status"] == 201:
        return jsonify(response["data"]), response["status"]

    return jsonify({"message": response["message"]}), response["status"]

@tarefa_bp.route("/<int:tarefa_id>", methods=["PUT"])
def update_tarefa(tarefa_id):
    """
    Atualiza uma tarefa específica do banco de dados.
    ---
    tags:
      - Tarefas
    parameters:
      - in: path
        name: tarefa_id
        type: integer
        required: true
      - in: body
        name: tarefa
        schema:
          $ref: '#/definitions/TarefaSchema'
    responses:
      200:
        description: Tarefa atualizada com sucesso
        schema:
          $ref: '#/definitions/TarefaSchema'
      400:
        description: Erro ao atualizar tarefa
    """
    tarefa_data = request.get_json()

    response = update_tarefa_service(tarefa_id, tarefa_data)

    if response["status"] == 200:
        return jsonify(response["data"])

    return jsonify({"message": response["message"]}), response["status"]

@tarefa_bp.route("/<int:tarefa_id>", methods=["DELETE"])
def delete_tarefa(tarefa_id):
    """
    Deleta uma tarefa específica do banco de dados.
    ---
    tags:
      - Tarefas
    parameters:
      - in: path
        name: tarefa_id
        type: integer
        required: true
    responses:
      204:
        description: Tarefa deletada com sucesso
      404:
        description: Tarefa não encontrada
    """
    response = delete_tarefa_service(tarefa_id)

    return jsonify({"message": response["message"]}), response["status"]
