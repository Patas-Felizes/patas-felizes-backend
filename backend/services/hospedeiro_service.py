import logging
import traceback
from marshmallow import ValidationError

from backend.external.schemas import HospedeiroSchema
from backend.db import db
from backend.external.model import HospedeiroModel

# Crie um logger para este módulo (opcional, caso queira acompanhar logs)
logger = logging.getLogger(__name__)


def get_all_hospedeiros():
    """
    Consulta ao banco de dados para obter todos os hospedeiros
    """
    return HospedeiroModel.query.all()


def list_hospedeiros_service():
    """
    Retorna a lista de todos os hospedeiros armazenados no banco de dados.
    """
    try:
        hospedeiro_list = get_all_hospedeiros()

        if not hospedeiro_list:
            return {
                "status": 404,
                "message": "Nenhum hospedeiro encontrado no banco de dados.",
            }

        response_list = [hospedeiro.serialize for hospedeiro in hospedeiro_list]
        return {"status": 200, "data": response_list}

    except Exception as e:
        error_message = f"Erro ao listar hospedeiros: {str(e)}"
        traceback_message = traceback.format_exc()
        return {"status": 500, "message": error_message, "traceback": traceback_message}


def create_hospedeiro_service(hospedeiro_data: dict):
    """
    Cria um novo hospedeiro no banco de dados.
    """
    try:
        # Validação via schema (opcional usar HospedeiroSchema().load(hospedeiro_data))
        # Se quiser fazer a validação do Marshmallow explicitamente, use:
        # validated_data = HospedeiroSchema().load(hospedeiro_data)
        # E depois passe validated_data para o construtor do modelo.

        new_hospedeiro = HospedeiroModel(
            nome=hospedeiro_data["nome"],
            telefone=hospedeiro_data["telefone"],
            email=hospedeiro_data["email"],
            moradia=hospedeiro_data["moradia"],
        )

        db.session.add(new_hospedeiro)
        db.session.commit()

        return {"status": 201, "data": new_hospedeiro.serialize}

    except ValidationError as e:
        return {"status": 400, "message": str(e)}

    except Exception as e:
        error_message = f"Erro ao criar um novo hospedeiro: {str(e)}"
        traceback_message = traceback.format_exc()
        return {"status": 500, "message": error_message, "traceback": traceback_message}


def get_hospedeiro_service(hospedeiro_id: int):
    """
    Retorna um hospedeiro específico do banco de dados.
    """
    try:
        hospedeiro = HospedeiroModel.query.get(hospedeiro_id)

        if not hospedeiro:
            return {
                "status": 404,
                "message": "Hospedeiro não encontrado no banco de dados.",
            }

        return {"status": 200, "data": hospedeiro.serialize}

    except Exception as e:
        error_message = f"Erro ao consultar o hospedeiro: {str(e)}"
        traceback_message = traceback.format_exc()
        return {"status": 500, "message": error_message, "traceback": traceback_message}


def update_hospedeiro_service(hospedeiro_id: int, hospedeiro_data: dict):
    """
    Atualiza um hospedeiro específico no banco de dados.
    """
    try:
        hospedeiro_to_update = HospedeiroModel.query.get(hospedeiro_id)

        if not hospedeiro_to_update:
            return {
                "status": 404,
                "message": "Hospedeiro não encontrado no banco de dados.",
            }

        hospedeiro_to_update.nome = hospedeiro_data["nome"]
        hospedeiro_to_update.telefone = hospedeiro_data["telefone"]
        hospedeiro_to_update.email = hospedeiro_data["email"]
        hospedeiro_to_update.moradia = hospedeiro_data["moradia"]

        db.session.commit()

        return {"status": 200, "data": hospedeiro_to_update.serialize}

    except ValidationError as e:
        return {"status": 400, "message": str(e)}

    except Exception as e:
        error_message = f"Erro ao atualizar o hospedeiro: {str(e)}"
        traceback_message = traceback.format_exc()
        return {"status": 500, "message": error_message, "traceback": traceback_message}


def delete_hospedeiro_service(hospedeiro_id: int):
    """
    Deleta um hospedeiro específico do banco de dados.
    """
    try:
        hospedeiro_to_delete = HospedeiroModel.query.get(hospedeiro_id)

        if not hospedeiro_to_delete:
            return {
                "status": 404,
                "message": "Hospedeiro não encontrado no banco de dados.",
            }

        db.session.delete(hospedeiro_to_delete)
        db.session.commit()

        return {"status": 204, "message": "Hospedeiro deletado com sucesso."}

    except Exception as e:
        error_message = f"Erro ao deletar o hospedeiro: {str(e)}"
        traceback_message = traceback.format_exc()
        return {"status": 500, "message": error_message, "traceback": traceback_message}
