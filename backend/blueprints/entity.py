import logging
import traceback
from marshmallow import ValidationError
from backend.external.schemas import EntityIdSchema
from flask import Blueprint, Response, jsonify, request

from backend.db import db
from backend.external.model import EntityModel
from backend.services.entity_service import (
    get_entity_service,
    insert_entity_service,
    list_entities_service,
    list_entities_paginated_service
)
from backend.utils.decorators import jwt_required

logger = logging.getLogger(__name__)

entity = Blueprint("entity", __name__, url_prefix="/entity")


@entity.route("/entities", methods=["GET"])
@jwt_required
def get_entities(current_user):
    """
    Get Entity list
    ---
    tags:
      - Entity
    definitions:
      EntityResponse:
        type: object
        properties:
          entity_id:
            type: integer
            description: entity_id of Entity
          attr1:
            type: string
            description: attribute 1 of Entity
          attr2:
            type: string
            description: attribute 2 of Entity
    security:
      - APIKeyHeader: [ 'Authorization' ]
    responses:
      200:
        description: Success to get a list of Entity
        schema:
          $ref: '#/definitions/EntityResponse'
      400:
        description: Failed to get list of Entity
    """

    logger.info("Iniciando a consulta de entidades.")

    # Chama o serviço para listar as entidades
    service_response = list_entities_service()

    # Verifica o status da resposta do serviço e retorna a resposta apropriada
    if service_response["status"] == 200:
        logger.info("Consulta realizada com sucesso.")
        return jsonify(service_response["data"]), 200

    elif service_response["status"] == 404:
        logger.warning(service_response["message"])
        return jsonify({"message": service_response["message"]}), 404

    else:
        logger.error(service_response["message"])
        logger.debug(service_response["traceback"])
        return Response(service_response["message"], status=500)


@entity.route("/entities-paginated", methods=["GET"])
@jwt_required
def get_paginated_entities(current_user):
    """
    Get Entity list with pagination and links
    ---
    tags:
      - Entity
    parameters:
      - in: query
        name: page
        type: integer
        description: Número da página (padrão = 1)
      - in: query
        name: per_page
        type: integer
        description: Número de itens por página (padrão = 10)
    security:
      - APIKeyHeader: [ 'Authorization' ]
    responses:
      200:
        description: Sucesso ao obter lista paginada de entidades
        schema:
          type: object
          properties:
            data:
              type: array
              items:
                $ref: '#/definitions/EntityResponse'
            pagination:
              type: object
              properties:
                page:
                  type: integer
                per_page:
                  type: integer
                total_items:
                  type: integer
                total_pages:
                  type: integer
                next_page:
                  type: string
                  description: URL da próxima página
                prev_page:
                  type: string
                  description: URL da página anterior
      400:
        description: Falha ao obter lista de entidades
    """

    logger.info("Iniciando a consulta paginada de entidades.")

    # Obtém os parâmetros de paginação da query string
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)

    # Chama o serviço para listar as entidades com paginação
    service_response = list_entities_paginated_service(page, per_page)

    # Verifica o status da resposta do serviço e retorna a resposta apropriada
    if service_response["status"] == 200:
        logger.info("Consulta realizada com sucesso.")
        return jsonify({
            "data": service_response["data"],
            "pagination": service_response["pagination"]
        }), 200

    elif service_response["status"] == 404:
        logger.warning(service_response["message"])
        return jsonify({"message": service_response["message"]}), 404

    else:
        logger.error(service_response["message"])
        logger.debug(service_response["traceback"])
        return Response(service_response["message"], status=500)


@entity.route("/entity/<entity_id>", methods=["GET"])
@jwt_required
def get_entity(current_user,entity_id):
    """
    Get specific entity
    ---
    tags:
      - Entity
    parameters:
      - name: entity_id
        in: path
        type: integer
        required: true
        decription: entity_id of specific Entity
    security:
      - APIKeyHeader: [ 'Authorization' ]
    responses:
      200:
        description: Success to get specific Entity
        schema:
          $ref: '#/definitions/EntityResponse'
      400:
        description: Failed to get specific Entity
    """

    logger.info(f"Iniciando a consulta da entidade com entity_id {entity_id}.")

    try:

      # Instanciando o schema
      entity_id_schema = EntityIdSchema()
      # Valida o entity_id usando o schema do marshmallow
      data = entity_id_schema.load({"entity_id": entity_id})

      # Chama o serviço para obter a entidade pelo ID
      service_response = get_entity_service(entity_id)

      # Verifica o status retornado pelo serviço
      if service_response["status"] == 200:
          logger.info(f"Entidade com ID {id} encontrada e serializada com sucesso.")
          return jsonify(service_response["data"]), 200

      elif service_response["status"] == 400:
              logger.warning(f"Erro de validação: {service_response.get('errors')}")
              return jsonify({"message": service_response["message"], "errors": service_response.get("errors")}), service_response["status"]

      elif service_response["status"] == 404:
          logger.warning(service_response["message"])
          return jsonify({"message": service_response["message"]}), 404

      else:
          logger.error(service_response["message"])
          logger.debug(service_response["traceback"])
          return Response(service_response["message"], status=500)

    except ValidationError as ve:
        # Captura erros de validação e retorna uma resposta apropriada
        return {"status": 400,
                "message": "Erro de validação",
                "errors": ve.messages}


@entity.route("/entity", methods=["POST"])
@jwt_required
def insert_entity(current_user):
    """
    Insert Entity in the Cache
    ---
    tags:
      - Entity
    definitions:
      EntityBody:
        type: object
        properties:
          attr1:
            type: string
            description: total wave significant height
            example: value1
          attr2:
            type: number
            description: attr2 of the Entity
            example: 77
    security:
      - APIKeyHeader: [ 'Authorization' ]
    parameters:
      - name: body
        in: body
        required: true
        description: Entity parameters
        schema:
          $ref: '#/definitions/EntityBody'
    responses:
      200:
        description: Success to insert new Entity
        schema:
          $ref: '#/definitions/EntityBody'
      400:
        description: Failed to insert new Entity
    """
    try:
        logger.info("Recebendo os dados da nova entidade.")

        # Obter o JSON enviado no corpo da requisição
        content = request.get_json()

        # Chama o serviço para inserir a entidade
        service_response = insert_entity_service(content)

        # Verifica o status retornado pelo serviço
        if service_response["status"] == 200:
            logger.info(
                f"Entidade inserida com sucesso. ID da entidade: {service_response['data']['id']}"
            )
            return jsonify(service_response["data"]), 200

        elif service_response["status"] == 400:
            logger.warning(f"Erro de validação: {service_response.get('errors')}")
            return jsonify({"message": service_response["message"], "errors": service_response.get("errors")}), service_response["status"]

        else:
            logger.warning(service_response["message"])
            return (
                jsonify({"message": service_response["message"]}),
                service_response["status"],
            )

    except Exception as e:
        logger.error(f"Erro ao processar requisição: {str(e)}")
        logger.debug(f"Detalhes do erro: {traceback.format_exc()}")

        # Retornar uma resposta de erro detalhada
        return Response(
            f"Error processing request. Exception: {traceback.format_exc()}", status=500
        )
