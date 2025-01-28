import logging
import traceback
from marshmallow import ValidationError

from backend.external.schemas import ApadrinhamentoSchema
from backend.db import db
from backend.external.model import ApadrinhamentoModel

# Exemplo de logger para o módulo
logger = logging.getLogger(__name__)


def get_all_apadrinhamentos():
    """Consulta ao banco de dados para obter todos os apadrinhamentos."""
    return ApadrinhamentoModel.query.all()


def list_apadrinhamentos_service():
    """
    Retorna a lista de todos os apadrinhamentos armazenados no banco de dados.
    """
    try:
        apadrinhamento_list = get_all_apadrinhamentos()

        if not apadrinhamento_list:
            return {
                "status": 404,
                "message": "Nenhum apadrinhamento encontrado no banco de dados.",
            }

        response_list = [apadrinhamento.serialize for apadrinhamento in apadrinhamento_list]
        return {"status": 200, "data": response_list}

    except Exception as e:
        error_message = f"Erro ao listar apadrinhamentos: {str(e)}"
        traceback_message = traceback.format_exc()
        logger.error(error_message, exc_info=True)
        return {
            "status": 500,
            "message": error_message,
            "traceback": traceback_message
        }


def create_apadrinhamento_service(apadrinhamento_data: dict):
    """
    Cria um novo apadrinhamento no banco de dados.
    """
    try:
        # Exemplo de uso de schema (opcional, se você quiser validá-lo explicitamente)
        # ApadrinhamentoSchema().load(apadrinhamento_data)

        new_apadrinhamento = ApadrinhamentoModel(
            animal_id=apadrinhamento_data["animal_id"],
            nome_apadrinhador=apadrinhamento_data["nome_apadrinhador"],
            valor=apadrinhamento_data["valor"],
            regularidade=apadrinhamento_data["regularidade"],
        )

        db.session.add(new_apadrinhamento)
        db.session.commit()

        return {"status": 201, "data": new_apadrinhamento.serialize}

    except ValidationError as e:
        return {"status": 400, "message": str(e)}

    except Exception as e:
        error_message = f"Erro ao criar apadrinhamento: {str(e)}"
        traceback_message = traceback.format_exc()
        logger.error(error_message, exc_info=True)
        return {
            "status": 500,
            "message": error_message,
            "traceback": traceback_message
        }


def get_apadrinhamento_service(apadrinhamento_id: int):
    """
    Retorna um apadrinhamento específico do banco de dados.
    """
    try:
        apadrinhamento = ApadrinhamentoModel.query.get(apadrinhamento_id)

        if not apadrinhamento:
            return {
                "status": 404,
                "message": "Apadrinhamento não encontrado no banco de dados.",
            }

        return {"status": 200, "data": apadrinhamento.serialize}

    except Exception as e:
        error_message = f"Erro ao consultar o apadrinhamento: {str(e)}"
        traceback_message = traceback.format_exc()
        logger.error(error_message, exc_info=True)
        return {
            "status": 500,
            "message": error_message,
            "traceback": traceback_message
        }


def update_apadrinhamento_service(apadrinhamento_id: int, apadrinhamento_data: dict):
    """
    Atualiza um apadrinhamento específico no banco de dados.
    """
    try:
        apadrinhamento_to_update = ApadrinhamentoModel.query.get(apadrinhamento_id)

        if not apadrinhamento_to_update:
            return {
                "status": 404,
                "message": "Apadrinhamento não encontrado no banco de dados.",
            }

        apadrinhamento_to_update.animal_id = apadrinhamento_data["animal_id"]
        apadrinhamento_to_update.nome_apadrinhador = apadrinhamento_data["nome_apadrinhador"]
        apadrinhamento_to_update.valor = apadrinhamento_data["valor"]
        apadrinhamento_to_update.regularidade = apadrinhamento_data["regularidade"]

        db.session.commit()

        return {"status": 200, "data": apadrinhamento_to_update.serialize}

    except ValidationError as e:
        return {"status": 400, "message": str(e)}

    except Exception as e:
        error_message = f"Erro ao atualizar o apadrinhamento: {str(e)}"
        traceback_message = traceback.format_exc()
        logger.error(error_message, exc_info=True)
        return {
            "status": 500,
            "message": error_message,
            "traceback": traceback_message
        }


def delete_apadrinhamento_service(apadrinhamento_id: int):
    """
    Deleta um apadrinhamento específico do banco de dados.
    """
    try:
        apadrinhamento_to_delete = ApadrinhamentoModel.query.get(apadrinhamento_id)

        if not apadrinhamento_to_delete:
            return {
                "status": 404,
                "message": "Apadrinhamento não encontrado no banco de dados.",
            }

        db.session.delete(apadrinhamento_to_delete)
        db.session.commit()

        return {"status": 204, "message": "Apadrinhamento deletado com sucesso."}

    except Exception as e:
        error_message = f"Erro ao deletar o apadrinhamento: {str(e)}"
        traceback_message = traceback.format_exc()
        logger.error(error_message, exc_info=True)
        return {
            "status": 500,
            "message": error_message,
            "traceback": traceback_message
        }
