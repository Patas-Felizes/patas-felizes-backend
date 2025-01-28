import logging
import traceback
from marshmallow import ValidationError

from backend.external.schemas import DoacaoSchema
from backend.db import db
from backend.external.model import DoacaoModel

# Create logger for this module
logger = logging.getLogger(__name__)


def get_all_doacoes():
    # Consulta ao banco de dados para obter todas as doações
    doacao_list = DoacaoModel.query.all()

    return doacao_list


def list_doacoes_service():
    """
    Retorna a lista de todas as doações armazenadas no banco de dados.
    """
    try:
        # Consulta ao banco de dados para obter todas as doações
        doacao_list = get_all_doacoes()

        # Verifica se a lista está vazia
        if not doacao_list:
            return {
                "status": 404,
                "message": "Nenhuma doação encontrada no banco de dados.",
            }

        # Serializa as doações
        response_list = [doacao.serialize for doacao in doacao_list]

        # Retorna os dados serializados e o status de sucesso
        return {"status": 200, "data": response_list}

    except Exception as e:
        # Se ocorrer qualquer erro, retorna um dicionário com o erro e o traceback
        error_message = f"Erro ao consultar ou listar doações: {str(e)}"
        traceback_message = traceback.format_exc()
        return {"status": 500, "message": error_message, "traceback": traceback_message}


def create_doacao_service(doacao: DoacaoSchema):
    """
    Cria uma nova doação no banco de dados.
    """
    try:
        # Cria uma nova instância do modelo DoacaoModel
        new_doacao = DoacaoModel(
            doador=doacao["doador"],
            valor=doacao["valor"],
            data_doacao=doacao["data_doacao"],
            animal_id=doacao["animal_id"],
            companha_id=doacao["companha_id"],
            estoque_id=doacao["estoque_id"],
            comprovante=doacao["comprovante"],
        )

        # Adiciona a nova doação ao banco de dados
        db.session.add(new_doacao)
        db.session.commit()

        # Retorna a doação criada com sucesso
        return {"status": 201, "data": new_doacao.serialize}

    except ValidationError as e:
        # Se ocorrer um erro de validação, retorna uma mensagem de erro
        return {"status": 400, "message": str(e)}

    except Exception as e:
        # Se ocorrer qualquer outro erro, retorna uma mensagem de erro com o traceback
        error_message = f"Erro ao criar uma nova doação: {str(e)}"
        traceback_message = traceback.format_exc()
        return {"status": 500, "message": error_message, "traceback": traceback_message}


def get_doacao_service(doacao_id: int):
    """
    Retorna uma doação específica do banco de dados.
    """
    try:
        # Consulta ao banco de dados para obter a doação com o ID fornecido
        doacao = DoacaoModel.query.get(doacao_id)

        # Verifica se a doação existe
        if not doacao:
            return {"status": 404, "message": "Doação não encontrada no banco de dados."}

        # Retorna a doação encontrada e o status de sucesso
        return {"status": 200, "data": doacao.serialize}

    except Exception as e:
        # Se ocorrer qualquer erro, retorna uma mensagem de erro com o traceback
        error_message = f"Erro ao consultar a doação: {str(e)}"
        traceback_message = traceback.format_exc()
        return {"status": 500, "message": error_message, "traceback": traceback_message}


def update_doacao_service(doacao_id: int, doacao: DoacaoSchema):
    """
    Atualiza uma doação específica no banco de dados.
    """
    try:
        # Consulta ao banco de dados para obter a doação com o ID fornecido
        doacao_to_update = DoacaoModel.query.get(doacao_id)

        # Verifica se a doação existe
        if not doacao_to_update:
            return {"status": 404, "message": "Doação não encontrada no banco de dados."}

        # Atualiza os dados da doação
        doacao_to_update.doador = doacao["doador"]
        doacao_to_update.valor = doacao["valor"]
        doacao_to_update.data_doacao = doacao["data_doacao"]
        doacao_to_update.animal_id = doacao["animal_id"]
        doacao_to_update.companha_id = doacao["companha_id"]
        doacao_to_update.estoque_id = doacao["estoque_id"]
        doacao_to_update.comprovante = doacao["comprovante"]

        # Salva as alterações no banco de dados
        db.session.commit()

        # Retorna a doação atualizada e o status de sucesso
        return {"status": 200, "data": doacao_to_update.serialize}

    except ValidationError as e:
        # Se ocorrer um erro de validação, retorna uma mensagem de erro
        return {"status": 400, "message": str(e)}

    except Exception as e:
        # Se ocorrer qualquer outro erro, retorna uma mensagem de erro com o traceback
        error_message = f"Erro ao atualizar a doação: {str(e)}"
        traceback_message = traceback.format_exc()
        return {"status": 500, "message": error_message, "traceback": traceback_message}


def delete_doacao_service(doacao_id: int):
    """
    Deleta uma doação específica do banco de dados.
    """
    try:
        # Consulta ao banco de dados para obter a doação com o ID fornecido
        doacao_to_delete = DoacaoModel.query.get(doacao_id)

        # Verifica se a doação existe
        if not doacao_to_delete:
            return {"status": 404, "message": "Doação não encontrada no banco de dados."}

        # Deleta a doação do banco de dados
        db.session.delete(doacao_to_delete)
        db.session.commit()

        # Retorna o status de sucesso
        return {"status": 204, "message": "Doação deletada com sucesso."}

    except Exception as e:
        # Se ocorrer qualquer erro, retorna uma mensagem de erro com o traceback
        error_message = f"Erro ao deletar a doação: {str(e)}"
        traceback_message = traceback.format_exc()
        return {"status": 500, "message": error_message, "traceback": traceback_message}
