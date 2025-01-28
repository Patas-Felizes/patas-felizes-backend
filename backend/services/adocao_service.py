import logging
import traceback
from marshmallow import ValidationError

from backend.external.schemas import AdocaoSchema
from backend.db import db
from backend.external.model import AdocaoModel

# Create logger for this module
logger = logging.getLogger(__name__)


def get_all_adocoes():
    """
    Consulta ao banco de dados para obter todas as adoções.
    """
    return AdocaoModel.query.all()


def list_adocoes_service():
    """
    Retorna a lista de todas as adoções armazenadas no banco de dados.
    """
    try:
        adocao_list = get_all_adocoes()

        if not adocao_list:
            return {
                "status": 404,
                "message": "Nenhuma adoção encontrada no banco de dados.",
            }

        response_list = [adocao.serialize for adocao in adocao_list]
        return {"status": 200, "data": response_list}

    except Exception as e:
        error_message = f"Erro ao consultar ou listar adoções: {str(e)}"
        traceback_message = traceback.format_exc()
        logger.error(error_message)
        logger.debug(traceback_message)
        return {"status": 500, "message": error_message, "traceback": traceback_message}


def create_adocao_service(adocao_data: AdocaoSchema):
    """
    Cria uma nova adoção no banco de dados.
    """
    try:
        new_adocao = AdocaoModel(
            animal_id=adocao_data["animal_id"],
            adotante_id=adocao_data["adotante_id"],
            companha_id=adocao_data["companha_id"],
            data_devolucao=adocao_data["data_devolucao"],
            motivo_devolucao=adocao_data["motivo_devolucao"],
            data_adocao=adocao_data["data_adocao"],
            data_cadastro=adocao_data["data_cadastro"],
        )

        db.session.add(new_adocao)
        db.session.commit()

        return {"status": 201, "data": new_adocao.serialize}

    except ValidationError as e:
        return {"status": 400, "message": str(e)}

    except Exception as e:
        error_message = f"Erro ao criar uma nova adoção: {str(e)}"
        traceback_message = traceback.format_exc()
        logger.error(error_message)
        logger.debug(traceback_message)
        return {"status": 500, "message": error_message, "traceback": traceback_message}


def get_adocao_service(adocao_id: int):
    """
    Retorna uma adoção específica do banco de dados.
    """
    try:
        adocao = AdocaoModel.query.get(adocao_id)

        if not adocao:
            return {"status": 404, "message": "Adoção não encontrada no banco de dados."}

        return {"status": 200, "data": adocao.serialize}

    except Exception as e:
        error_message = f"Erro ao consultar a adoção: {str(e)}"
        traceback_message = traceback.format_exc()
        logger.error(error_message)
        logger.debug(traceback_message)
        return {"status": 500, "message": error_message, "traceback": traceback_message}


def update_adocao_service(adocao_id: int, adocao_data: AdocaoSchema):
    """
    Atualiza uma adoção específica no banco de dados.
    """
    try:
        adocao_to_update = AdocaoModel.query.get(adocao_id)

        if not adocao_to_update:
            return {"status": 404, "message": "Adoção não encontrada no banco de dados."}

        adocao_to_update.animal_id = adocao_data["animal_id"]
        adocao_to_update.adotante_id = adocao_data["adotante_id"]
        adocao_to_update.companha_id = adocao_data["companha_id"]
        adocao_to_update.data_devolucao = adocao_data["data_devolucao"]
        adocao_to_update.motivo_devolucao = adocao_data["motivo_devolucao"]
        adocao_to_update.data_adocao = adocao_data["data_adocao"]
        adocao_to_update.data_cadastro = adocao_data["data_cadastro"]

        db.session.commit()

        return {"status": 200, "data": adocao_to_update.serialize}

    except ValidationError as e:
        return {"status": 400, "message": str(e)}

    except Exception as e:
        error_message = f"Erro ao atualizar a adoção: {str(e)}"
        traceback_message = traceback.format_exc()
        logger.error(error_message)
        logger.debug(traceback_message)
        return {"status": 500, "message": error_message, "traceback": traceback_message}


def delete_adocao_service(adocao_id: int):
    """
    Deleta uma adoção específica do banco de dados.
    """
    try:
        adocao_to_delete = AdocaoModel.query.get(adocao_id)

        if not adocao_to_delete:
            return {"status": 404, "message": "Adoção não encontrada no banco de dados."}

        db.session.delete(adocao_to_delete)
        db.session.commit()

        return {"status": 204, "message": "Adoção deletada com sucesso."}

    except Exception as e:
        error_message = f"Erro ao deletar a adoção: {str(e)}"
        traceback_message = traceback.format_exc()
        logger.error(error_message)
        logger.debug(traceback_message)
        return {"status": 500, "message": error_message, "traceback": traceback_message}
