import logging
import traceback
from marshmallow import ValidationError

from backend.external.schemas import EntitySchema
from backend.db import db
from backend.external.model import (
    EntityModel,  # Certifique-se de que o modelo está corretamente importado
)

from backend.utils.pagination import build_pagination

# Create logger for this module
logger = logging.getLogger(__name__)


def get_all_entities():
    # Consulta ao banco de dados para obter todas as entidades
    entity_list = EntityModel.query.all()

    return entity_list


def list_entities_service():
    """
    Retorna a lista de todas as entidades armazenadas no banco de dados.
    """
    try:
        # Consulta ao banco de dados para obter todas as entidades
        entity_list = get_all_entities()

        # Verifica se a lista está vazia
        if not entity_list:
            return {
                "status": 404,
                "message": "Nenhuma entidade encontrada no banco de dados.",
            }

        # Serializa as entidades
        response_list = [entity.serialize for entity in entity_list]

        # Retorna os dados serializados e o status de sucesso
        return {"status": 200, "data": response_list}

    except Exception as e:
        # Se ocorrer qualquer erro, retorna um dicionário com o erro e o traceback
        error_message = f"Erro ao consultar ou listar entidades: {str(e)}"
        traceback_message = traceback.format_exc()
        return {"status": 500, "message": error_message, "traceback": traceback_message}


def get_paginated_entities(page, per_page):
    # Consulta ao banco de dados com paginação
    paginated_entities = EntityModel.query.paginate(page=page, per_page=per_page, error_out=False)

    return paginated_entities


def list_entities_paginated_service(page, per_page):
    """
    Retorna a lista paginada de todas as entidades armazenadas no banco de dados.
    """
    try:
        # Consulta ao banco de dados com paginação
        paginated_entities = get_paginated_entities(page, per_page)

        # Verifica se a lista está vazia
        if not paginated_entities.items:
            return {
                "status": 404,
                "message": f"Nenhuma entidade encontrada no banco de dados para a página {page} com {per_page} itens por página.",
            }

        # Serializa as entidades
        response_list = [entity.serialize for entity in paginated_entities.items]

        # Extrai os dados relevantes de paginação
        pagination_info = build_pagination(
            page=paginated_entities.page,
            per_page=paginated_entities.per_page,
            total_items=paginated_entities.total,
            total_pages=paginated_entities.pages,
            has_next=paginated_entities.has_next,
            has_prev=paginated_entities.has_prev,
            next_num=paginated_entities.next_num,
            prev_num=paginated_entities.prev_num
        )

        # Retorna os dados serializados e informações de paginação
        return {
            "status": 200,
            "data": response_list,
            "pagination": pagination_info
        }

    except Exception as e:
        # Se ocorrer qualquer erro, retorna um dicionário com o erro e o traceback
        error_message = f"Erro ao consultar ou listar entidades: {str(e)}"
        traceback_message = traceback.format_exc()
        return {"status": 500, "message": error_message, "traceback": traceback_message}


def get_entity_by_id(entity_id):
    entity_db_obj = EntityModel.query.filter(EntityModel.entity_id == entity_id).first()
    return entity_db_obj


def get_entity_service(entity_id):
    """
    Obtém uma entidade específica pelo seu ID.
    """
    try:
        # Consulta ao banco de dados para encontrar a entidade pelo ID
        entity_db_obj = get_entity_by_id(entity_id)

        # Verifica se a entidade foi encontrada
        if not entity_db_obj:
            return {
                "status": 404,
                "message": f"Entidade com ID {entity_id} não foi encontrada.",
            }

        # Serializa a entidade
        entity_obj = entity_db_obj.serialize
        return {"status": 200, "data": entity_obj}

    except Exception as e:
        # Retorna erro em caso de exceção
        error_message = f"Erro ao consultar a entidade com ID {entity_id}: {str(e)}"
        traceback_message = traceback.format_exc()
        return {"status": 500, "message": error_message, "traceback": traceback_message}

def insert_entity_service(content):
    """
    Função de serviço para inserir uma nova entidade no banco de dados.
    """
    try:

        # Instancia o schema
        schema = EntitySchema()

        # Valida os dados recebidos
        data = schema.load(content)

        # Cria o objeto da entidade com os valores recebidos (sem 'id')
        entity_obj = EntityModel(attr1=content.get("attr1"), attr2=content.get("attr2"))

        # Adiciona a entidade ao banco de dados e comita
        db.session.add(entity_obj)
        db.session.commit()

        # Retorna a entidade criada
        return {
            "status": 200,
            "data": {
                "id": entity_obj.entity_id,  # O ID gerado automaticamente será retornado
                "attr1": entity_obj.attr1,
                "attr2": entity_obj.attr2,
            },
        }

    except ValidationError as ve:
        # Captura erros de validação e retorna uma resposta apropriada
        return {
            "status": 400,
            "message": "Erro de validação",
            "errors": ve.messages,
        }

    except Exception as e:
        # Captura a exceção e retorna a mensagem de erro
        error_message = f"Erro ao inserir dados da entidade: {str(e)}"
        traceback_message = traceback.format_exc()
        return {"status": 500, "message": error_message, "traceback": traceback_message}



