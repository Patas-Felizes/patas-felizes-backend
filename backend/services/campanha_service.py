import logging
import traceback
from marshmallow import ValidationError

from backend.external.schemas import CampanhaSchema
from backend.db import db
from backend.external.model import CampanhaModel

logger = logging.getLogger(__name__)

def get_all_campanhas():
    """
    Retorna todas as campanhas do banco de dados.
    """
    campanha_list = CampanhaModel.query.all()
    return campanha_list


def list_campanhas_service():
    """
    Retorna a lista de todas as campanhas armazenadas no banco de dados.
    """
    try:
        campanha_list = get_all_campanhas()

        if not campanha_list:
            return {
                "status": 404,
                "message": "Nenhuma campanha encontrada no banco de dados.",
            }

        response_list = [campanha.serialize for campanha in campanha_list]

        return {"status": 200, "data": response_list}

    except Exception as e:
        error_message = f"Erro ao consultar ou listar campanhas: {str(e)}"
        traceback_message = traceback.format_exc()
        return {"status": 500, "message": error_message, "traceback": traceback_message}


def create_campanha_service(campanha: CampanhaSchema):
    """
    Cria uma nova campanha no banco de dados.
    """
    try:
        new_campanha = CampanhaModel(
            nome=campanha["nome"],
            tipo=campanha["tipo"],
            data_inicio=campanha["data_inicio"],
            data_termino=campanha["data_termino"],
            descricao=campanha["descricao"],
            local=campanha["local"],
        )

        db.session.add(new_campanha)
        db.session.commit()

        return {"status": 201, "data": new_campanha.serialize}

    except ValidationError as e:
        return {"status": 400, "message": str(e)}

    except Exception as e:
        error_message = f"Erro ao criar uma nova campanha: {str(e)}"
        traceback_message = traceback.format_exc()
        return {"status": 500, "message": error_message, "traceback": traceback_message}


def get_campanha_service(campanha_id: int):
    """
    Retorna uma campanha específica do banco de dados.
    """
    try:
        campanha = CampanhaModel.query.get(campanha_id)
        if not campanha:
            return {"status": 404, "message": "Campanha não encontrada no banco de dados."}

        return {"status": 200, "data": campanha.serialize}

    except Exception as e:
        error_message = f"Erro ao consultar a campanha: {str(e)}"
        traceback_message = traceback.format_exc()
        return {"status": 500, "message": error_message, "traceback": traceback_message}


def update_campanha_service(campanha_id: int, data: CampanhaSchema):
    """
    Atualiza uma campanha específica no banco de dados.
    """
    try:
        campanha_to_update = CampanhaModel.query.get(campanha_id)
        if not campanha_to_update:
            return {"status": 404, "message": "Campanha não encontrada no banco de dados."}

        campanha_to_update.nome = data["nome"]
        campanha_to_update.tipo = data["tipo"]
        campanha_to_update.data_inicio = data["data_inicio"]
        campanha_to_update.data_termino = data["data_termino"]
        campanha_to_update.descricao = data["descricao"]
        campanha_to_update.local = data["local"]

        db.session.commit()

        return {"status": 200, "data": campanha_to_update.serialize}

    except ValidationError as e:
        return {"status": 400, "message": str(e)}

    except Exception as e:
        error_message = f"Erro ao atualizar a campanha: {str(e)}"
        traceback_message = traceback.format_exc()
        return {"status": 500, "message": error_message, "traceback": traceback_message}


def delete_campanha_service(campanha_id: int):
    """
    Deleta uma campanha específica do banco de dados.
    """
    try:
        campanha_to_delete = CampanhaModel.query.get(campanha_id)
        if not campanha_to_delete:
            return {"status": 404, "message": "Campanha não encontrada no banco de dados."}

        db.session.delete(campanha_to_delete)
        db.session.commit()

        return {"status": 204, "message": "Campanha deletada com sucesso."}

    except Exception as e:
        error_message = f"Erro ao deletar a campanha: {str(e)}"
        traceback_message = traceback.format_exc()
        return {"status": 500, "message": error_message, "traceback": traceback_message}
