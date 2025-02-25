import logging
import traceback
from marshmallow import ValidationError

from backend.db import db
from backend.external.schemas import ProcedimentoSchema
from backend.external.model import ProcedimentoModel

logger = logging.getLogger(__name__)

def get_all_procedimentos():
    """
    Consulta todos os procedimentos no banco de dados.
    """
    return ProcedimentoModel.query.all()


def list_procedimentos_service():
    """
    Retorna a lista de todos os procedimentos armazenados no banco de dados.
    """
    try:
        procedimentos = get_all_procedimentos()

        if not procedimentos:
            return {
                "status": 404,
                "message": "Nenhum procedimento encontrado no banco de dados."
            }

        response_list = [p.serialize for p in procedimentos]
        return {"status": 200, "data": response_list}

    except Exception as e:
        error_message = f"Erro ao listar procedimentos: {str(e)}"
        traceback_message = traceback.format_exc()
        logger.error(error_message)
        return {"status": 500, "message": error_message, "traceback": traceback_message}


def get_procedimento_service(procedimento_id: int):
    """
    Retorna um procedimento específico do banco de dados.
    """
    try:
        procedimento = ProcedimentoModel.query.get(procedimento_id)
        if not procedimento:
            return {"status": 404, "message": "Procedimento não encontrado."}

        return {"status": 200, "data": procedimento.serialize}

    except Exception as e:
        error_message = f"Erro ao consultar procedimento: {str(e)}"
        traceback_message = traceback.format_exc()
        logger.error(error_message)
        return {"status": 500, "message": error_message, "traceback": traceback_message}


def create_procedimento_service(data: dict):
    """
    Cria um novo procedimento no banco de dados.
    """
    try:
        # Valida os dados usando o schema
        procedimento_schema = ProcedimentoSchema()
        procedimento_validado = procedimento_schema.load(data)

        new_procedimento = ProcedimentoModel(
            tipo=procedimento_validado["tipo"],
            descricao=procedimento_validado["descricao"],
            valor=procedimento_validado["valor"],
            data_procedimento=procedimento_validado["data_procedimento"],
            animal_id=procedimento_validado["animal_id"],
            voluntario_id=procedimento_validado["voluntario_id"],
        )
        
        db.session.add(new_procedimento)
        db.session.commit()

        return {"status": 201, "data": new_procedimento.serialize}

    except ValidationError as e:
        logger.error(f"Erro de validação ao criar procedimento: {e}")
        return {"status": 400, "message": str(e)}

    except Exception as e:
        error_message = f"Erro ao criar procedimento: {str(e)}"
        traceback_message = traceback.format_exc()
        logger.error(error_message)
        return {"status": 500, "message": error_message, "traceback": traceback_message}


def update_procedimento_service(procedimento_id: int, data: dict):
    """
    Atualiza um procedimento específico no banco de dados.
    """
    try:
        procedimento = ProcedimentoModel.query.get(procedimento_id)
        if not procedimento:
            return {"status": 404, "message": "Procedimento não encontrado."}

        procedimento_schema = ProcedimentoSchema()
        procedimento_validado = procedimento_schema.load(data, partial=True)

        procedimento.tipo = procedimento_validado.get("tipo", procedimento.tipo)
        procedimento.descricao = procedimento_validado.get("descricao", procedimento.descricao)
        procedimento.valor = procedimento_validado.get("valor", procedimento.valor)
        procedimento.data_procedimento = procedimento_validado.get("data_procedimento", procedimento.data_procedimento)
        procedimento.animal_id = procedimento_validado.get("animal_id", procedimento.animal_id)
        procedimento.voluntario_id = procedimento_validado.get("voluntario_id", procedimento.voluntario_id)

        db.session.commit()
        return {"status": 200, "data": procedimento.serialize}

    except ValidationError as e:
        logger.error(f"Erro de validação ao atualizar procedimento: {e}")
        return {"status": 400, "message": str(e)}

    except Exception as e:
        error_message = f"Erro ao atualizar procedimento: {str(e)}"
        traceback_message = traceback.format_exc()
        logger.error(error_message)
        return {"status": 500, "message": error_message, "traceback": traceback_message}


def delete_procedimento_service(procedimento_id: int):
    """
    Deleta um procedimento específico do banco de dados.
    """
    try:
        procedimento = ProcedimentoModel.query.get(procedimento_id)
        if not procedimento:
            return {"status": 404, "message": "Procedimento não encontrado."}

        db.session.delete(procedimento)
        db.session.commit()

        return {"status": 204, "message": "Procedimento deletado com sucesso."}

    except Exception as e:
        error_message = f"Erro ao deletar procedimento: {str(e)}"
        traceback_message = traceback.format_exc()
        logger.error(error_message)
        return {"status": 500, "message": error_message, "traceback": traceback_message}
