import logging
import traceback
from marshmallow import ValidationError

from backend.external.schemas import DespesaSchema
from backend.db import db
from backend.external.model import DespesaModel

logger = logging.getLogger(__name__)


def get_all_despesas():
    # Consulta ao banco de dados para obter todas as despesas
    despesa_list = DespesaModel.query.all()

    return despesa_list


def list_despesas_service():
    """
    Retorna a lista de todas as despesas armazenadas no banco de dados.
    """
    try:
        despesa_list = get_all_despesas()

        if not despesa_list:
            return {
                "status": 404,
                "message": "Nenhuma despesa encontrada no banco de dados.",
            }

        response_list = [despesa.serialize for despesa in despesa_list]

        return {"status": 200, "data": response_list}

    except Exception as e:
        error_message = f"Erro ao consultar ou listar despesas: {str(e)}"
        traceback_message = traceback.format_exc()
        return {"status": 500, "message": error_message, "traceback": traceback_message}


def create_despesa_service(despesa: DespesaSchema):
    """
    Cria uma nova despesa no banco de dados.
    """
    try:
        new_despesa = DespesaModel(
            valor=despesa["valor"],
            data_despesa=despesa["data_despesa"],
            tipo=despesa["tipo"],
            animal_id=despesa["animal_id"],
            procedimento_id=despesa["procedimento_id"],
            comprovante=despesa["comprovante"],
        )

        db.session.add(new_despesa)
        db.session.commit()

        return {"status": 201, "data": new_despesa.serialize}

    except ValidationError as e:
        return {"status": 400, "message": str(e)}

    except Exception as e:
        error_message = f"Erro ao criar uma nova despesa: {str(e)}"
        traceback_message = traceback.format_exc()
        return {"status": 500, "message": error_message, "traceback": traceback_message}


def get_despesa_service(despesa_id: int):
    """
    Retorna uma despesa específica do banco de dados.
    """
    try:
        despesa = DespesaModel.query.get(despesa_id)

        if not despesa:
            return {"status": 404, "message": "Despesa não encontrada no banco de dados."}

        return {"status": 200, "data": despesa.serialize}

    except Exception as e:
        error_message = f"Erro ao consultar a despesa: {str(e)}"
        traceback_message = traceback.format_exc()
        return {"status": 500, "message": error_message, "traceback": traceback_message}


def update_despesa_service(despesa_id: int, despesa: DespesaSchema):
    """
    Atualiza uma despesa específica no banco de dados.
    """
    try:
        despesa_to_update = DespesaModel.query.get(despesa_id)

        if not despesa_to_update:
            return {"status": 404, "message": "Despesa não encontrada no banco de dados."}

        despesa_to_update.valor = despesa["valor"]
        despesa_to_update.data_despesa = despesa["data_despesa"]
        despesa_to_update.tipo = despesa["tipo"]
        despesa_to_update.animal_id = despesa["animal_id"]
        despesa_to_update.procedimento_id = despesa["procedimento_id"]
        despesa_to_update.comprovante = despesa["comprovante"]

        db.session.commit()

        return {"status": 200, "data": despesa_to_update.serialize}

    except ValidationError as e:
        return {"status": 400, "message": str(e)}

    except Exception as e:
        error_message = f"Erro ao atualizar a despesa: {str(e)}"
        traceback_message = traceback.format_exc()
        return {"status": 500, "message": error_message, "traceback": traceback_message}


def delete_despesa_service(despesa_id: int):
    """
    Deleta uma despesa específica do banco de dados.
    """
    try:
        despesa_to_delete = DespesaModel.query.get(despesa_id)

        if not despesa_to_delete:
            return {"status": 404, "message": "Despesa não encontrada no banco de dados."}

        db.session.delete(despesa_to_delete)
        db.session.commit()

        return {"status": 204, "message": "Despesa deletada com sucesso."}

    except Exception as e:
        error_message = f"Erro ao deletar a despesa: {str(e)}"
        traceback_message = traceback.format_exc()
        return {"status": 500, "message": error_message, "traceback": traceback_message}
