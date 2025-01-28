import logging
import traceback
from marshmallow import ValidationError

from backend.external.schemas import EstoqueSchema
from backend.db import db
from backend.external.model import EstoqueModel

# Create logger for this module
logger = logging.getLogger(__name__)

def get_all_estoque():
    # Consulta ao banco de dados para obter todos os itens de estoque
    estoque_list = EstoqueModel.query.all()
    return estoque_list

def list_estoque_service():
    """
    Retorna a lista de todos os itens no estoque.
    """
    try:
        # Consulta ao banco de dados para obter todos os itens
        estoque_list = get_all_estoque()

        # Verifica se a lista está vazia
        if not estoque_list:
            return {
                "status": 404,
                "message": "Nenhum item encontrado no estoque.",
            }

        # Serializa os itens
        response_list = [estoque.serialize for estoque in estoque_list]

        # Retorna os dados serializados e o status de sucesso
        return {"status": 200, "data": response_list}

    except Exception as e:
        error_message = f"Erro ao listar itens no estoque: {str(e)}"
        traceback_message = traceback.format_exc()
        return {"status": 500, "message": error_message, "traceback": traceback_message}

def create_estoque_service(estoque_data: EstoqueSchema):
    """
    Cria um novo item no estoque.
    """
    try:
        new_estoque = EstoqueModel(
            categoria=estoque_data["categoria"],
            tipo_item=estoque_data["tipo_item"],
            descricao=estoque_data["descricao"],
            especie_animal=estoque_data["especie_animal"],
            quantidade=estoque_data["quantidade"],
            quantidade_total=estoque_data["quantidade_total"],
        )

        # Adiciona ao banco de dados
        db.session.add(new_estoque)
        db.session.commit()

        return {"status": 201, "data": new_estoque.serialize}

    except ValidationError as e:
        return {"status": 400, "message": str(e)}

    except Exception as e:
        error_message = f"Erro ao criar item no estoque: {str(e)}"
        traceback_message = traceback.format_exc()
        return {"status": 500, "message": error_message, "traceback": traceback_message}

def get_estoque_service(estoque_id: int):
    """
    Retorna um item específico do estoque.
    """
    try:
        estoque = EstoqueModel.query.get(estoque_id)

        if not estoque:
            return {"status": 404, "message": "Item não encontrado no estoque."}

        return {"status": 200, "data": estoque.serialize}

    except Exception as e:
        error_message = f"Erro ao consultar o item no estoque: {str(e)}"
        traceback_message = traceback.format_exc()
        return {"status": 500, "message": error_message, "traceback": traceback_message}

def update_estoque_service(estoque_id: int, estoque_data: EstoqueSchema):
    """
    Atualiza um item específico do estoque.
    """
    try:
        estoque_to_update = EstoqueModel.query.get(estoque_id)

        if not estoque_to_update:
            return {"status": 404, "message": "Item não encontrado no estoque."}

        estoque_to_update.categoria = estoque_data["categoria"]
        estoque_to_update.tipo_item = estoque_data["tipo_item"]
        estoque_to_update.descricao = estoque_data["descricao"]
        estoque_to_update.especie_animal = estoque_data["especie_animal"]
        estoque_to_update.quantidade = estoque_data["quantidade"]
        estoque_to_update.quantidade_total = estoque_data["quantidade_total"]

        db.session.commit()

        return {"status": 200, "data": estoque_to_update.serialize}

    except ValidationError as e:
        return {"status": 400, "message": str(e)}

    except Exception as e:
        error_message = f"Erro ao atualizar o item no estoque: {str(e)}"
        traceback_message = traceback.format_exc()
        return {"status": 500, "message": error_message, "traceback": traceback_message}

def delete_estoque_service(estoque_id: int):
    """
    Deleta um item específico do estoque.
    """
    try:
        estoque_to_delete = EstoqueModel.query.get(estoque_id)

        if not estoque_to_delete:
            return {"status": 404, "message": "Item não encontrado no estoque."}

        db.session.delete(estoque_to_delete)
        db.session.commit()

        return {"status": 204, "message": "Item deletado com sucesso."}

    except Exception as e:
        error_message = f"Erro ao deletar o item no estoque: {str(e)}"
        traceback_message = traceback.format_exc()
        return {"status": 500, "message": error_message, "traceback": traceback_message}
