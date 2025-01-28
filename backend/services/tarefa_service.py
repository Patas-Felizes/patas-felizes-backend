import logging
import traceback
from marshmallow import ValidationError

from backend.external.schemas import TarefaSchema
from backend.db import db
from backend.external.model import TarefaModel

# Logger para o módulo
logger = logging.getLogger(__name__)

def get_all_tarefas():
    # Consulta ao banco de dados para obter todas as tarefas
    tarefa_list = TarefaModel.query.all()
    return tarefa_list

def list_tarefas_service():
    """
    Retorna a lista de todas as tarefas armazenadas no banco de dados.
    """
    try:
        tarefa_list = get_all_tarefas()

        if not tarefa_list:
            return {
                "status": 404,
                "message": "Nenhuma tarefa encontrada no banco de dados.",
            }

        response_list = [tarefa.serialize for tarefa in tarefa_list]
        return {"status": 200, "data": response_list}

    except Exception as e:
        error_message = f"Erro ao consultar ou listar tarefas: {str(e)}"
        traceback_message = traceback.format_exc()
        return {"status": 500, "message": error_message, "traceback": traceback_message}

def get_tarefa_service(tarefa_id: int):
    """
    Retorna uma tarefa específica do banco de dados.
    """
    try:
        tarefa = TarefaModel.query.get(tarefa_id)

        if not tarefa:
            return {"status": 404, "message": "Tarefa não encontrada no banco de dados."}

        return {"status": 200, "data": tarefa.serialize}

    except Exception as e:
        error_message = f"Erro ao consultar a tarefa: {str(e)}"
        traceback_message = traceback.format_exc()
        return {"status": 500, "message": error_message, "traceback": traceback_message}

def create_tarefa_service(tarefa: TarefaSchema):
    """
    Cria uma nova tarefa no banco de dados.
    """
    try:
        new_tarefa = TarefaModel(
            tipo=tarefa["tipo"],
            descricao=tarefa["descricao"],
            data_tarefa=tarefa["data_tarefa"],
            voluntario_id=tarefa["voluntario_id"],
            animal_id=tarefa["animal_id"],
        )

        db.session.add(new_tarefa)
        db.session.commit()

        return {"status": 201, "data": new_tarefa.serialize}

    except ValidationError as e:
        return {"status": 400, "message": str(e)}

    except Exception as e:
        error_message = f"Erro ao criar uma nova tarefa: {str(e)}"
        traceback_message = traceback.format_exc()
        return {"status": 500, "message": error_message, "traceback": traceback_message}

def update_tarefa_service(tarefa_id: int, tarefa: TarefaSchema):
    """
    Atualiza uma tarefa específica no banco de dados.
    """
    try:
        tarefa_to_update = TarefaModel.query.get(tarefa_id)

        if not tarefa_to_update:
            return {"status": 404, "message": "Tarefa não encontrada no banco de dados."}

        tarefa_to_update.tipo = tarefa["tipo"]
        tarefa_to_update.descricao = tarefa["descricao"]
        tarefa_to_update.data_tarefa = tarefa["data_tarefa"]
        tarefa_to_update.voluntario_id = tarefa["voluntario_id"]
        tarefa_to_update.animal_id = tarefa["animal_id"]

        db.session.commit()

        return {"status": 200, "data": tarefa_to_update.serialize}

    except ValidationError as e:
        return {"status": 400, "message": str(e)}

    except Exception as e:
        error_message = f"Erro ao atualizar a tarefa: {str(e)}"
        traceback_message = traceback.format_exc()
        return {"status": 500, "message": error_message, "traceback": traceback_message}

def delete_tarefa_service(tarefa_id: int):
    """
    Deleta uma tarefa específica do banco de dados.
    """
    try:
        tarefa_to_delete = TarefaModel.query.get(tarefa_id)

        if not tarefa_to_delete:
            return {"status": 404, "message": "Tarefa não encontrada no banco de dados."}

        db.session.delete(tarefa_to_delete)
        db.session.commit()

        return {"status": 204, "message": "Tarefa deletada com sucesso."}

    except Exception as e:
        error_message = f"Erro ao deletar a tarefa: {str(e)}"
        traceback_message = traceback.format_exc()
        return {"status": 500, "message": error_message, "traceback": traceback_message}
