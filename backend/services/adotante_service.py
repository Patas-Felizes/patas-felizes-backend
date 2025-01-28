import logging
import traceback
from marshmallow import ValidationError

from backend.external.schemas import AdotanteSchema
from backend.db import db
from backend.external.model import AdotanteModel

logger = logging.getLogger(__name__)

def get_all_adotantes():
    """
    Consulta ao banco de dados para obter todos os adotantes.
    """
    return AdotanteModel.query.all()


def list_adotantes_service():
    """
    Retorna a lista de todos os adotantes armazenados no banco de dados.
    """
    try:
        adotante_list = get_all_adotantes()

        if not adotante_list:
            return {
                "status": 404,
                "message": "Nenhum adotante encontrado no banco de dados.",
            }

        response_list = [adotante.serialize for adotante in adotante_list]
        return {"status": 200, "data": response_list}

    except Exception as e:
        error_message = f"Erro ao consultar ou listar adotantes: {str(e)}"
        traceback_message = traceback.format_exc()
        logger.error(error_message)
        logger.debug(traceback_message)
        return {"status": 500, "message": error_message, "traceback": traceback_message}


def create_adotante_service(adotante_data: AdotanteSchema):
    """
    Cria um novo adotante no banco de dados.
    """
    try:
        new_adotante = AdotanteModel(
            nome=adotante_data["nome"],
            telefone=adotante_data["telefone"],
            email=adotante_data["email"],
            moradia=adotante_data["moradia"],
        )

        db.session.add(new_adotante)
        db.session.commit()

        return {"status": 201, "data": new_adotante.serialize}

    except ValidationError as e:
        return {"status": 400, "message": str(e)}

    except Exception as e:
        error_message = f"Erro ao criar um novo adotante: {str(e)}"
        traceback_message = traceback.format_exc()
        logger.error(error_message)
        logger.debug(traceback_message)
        return {"status": 500, "message": error_message, "traceback": traceback_message}


def get_adotante_service(adotante_id: int):
    """
    Retorna um adotante específico do banco de dados.
    """
    try:
        adotante = AdotanteModel.query.get(adotante_id)

        if not adotante:
            return {"status": 404, "message": "Adotante não encontrado no banco de dados."}

        return {"status": 200, "data": adotante.serialize}

    except Exception as e:
        error_message = f"Erro ao consultar o adotante: {str(e)}"
        traceback_message = traceback.format_exc()
        logger.error(error_message)
        logger.debug(traceback_message)
        return {"status": 500, "message": error_message, "traceback": traceback_message}


def update_adotante_service(adotante_id: int, adotante_data: AdotanteSchema):
    """
    Atualiza um adotante específico no banco de dados.
    """
    try:
        adotante_to_update = AdotanteModel.query.get(adotante_id)

        if not adotante_to_update:
            return {"status": 404, "message": "Adotante não encontrado no banco de dados."}

        adotante_to_update.nome = adotante_data["nome"]
        adotante_to_update.telefone = adotante_data["telefone"]
        adotante_to_update.email = adotante_data["email"]
        adotante_to_update.moradia = adotante_data["moradia"]

        db.session.commit()

        return {"status": 200, "data": adotante_to_update.serialize}

    except ValidationError as e:
        return {"status": 400, "message": str(e)}

    except Exception as e:
        error_message = f"Erro ao atualizar o adotante: {str(e)}"
        traceback_message = traceback.format_exc()
        logger.error(error_message)
        logger.debug(traceback_message)
        return {"status": 500, "message": error_message, "traceback": traceback_message}


def delete_adotante_service(adotante_id: int):
    """
    Deleta um adotante específico do banco de dados.
    """
    try:
        adotante_to_delete = AdotanteModel.query.get(adotante_id)

        if not adotante_to_delete:
            return {"status": 404, "message": "Adotante não encontrado no banco de dados."}

        db.session.delete(adotante_to_delete)
        db.session.commit()

        return {"status": 204, "message": "Adotante deletado com sucesso."}

    except Exception as e:
        error_message = f"Erro ao deletar o adotante: {str(e)}"
        traceback_message = traceback.format_exc()
        logger.error(error_message)
        logger.debug(traceback_message)
        return {"status": 500, "message": error_message, "traceback": traceback_message}
