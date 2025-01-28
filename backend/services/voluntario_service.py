import logging
import traceback
from marshmallow import ValidationError

from backend.external.schemas import VoluntarioSchema
from backend.db import db
from backend.external.model import VoluntarioModel

# Create logger for this module
logger = logging.getLogger(__name__)


def get_all_voluntarios():
    # Consulta ao banco de dados para obter todos os voluntários
    voluntario_list = VoluntarioModel.query.all()
    return voluntario_list


def list_voluntarios_service():
    """
    Retorna a lista de todos os voluntários armazenados no banco de dados.
    """
    try:
        # Consulta ao banco de dados para obter todos os voluntários
        voluntario_list = get_all_voluntarios()

        # Verifica se a lista está vazia
        if not voluntario_list:
            return {
                "status": 404,
                "message": "Nenhum voluntário encontrado no banco de dados.",
            }

        # Serializa os voluntários
        response_list = [voluntario.serialize for voluntario in voluntario_list]

        # Retorna os dados serializados e o status de sucesso
        return {"status": 200, "data": response_list}

    except Exception as e:
        # Se ocorrer qualquer erro, retorna um dicionário com o erro e o traceback
        error_message = f"Erro ao consultar ou listar voluntários: {str(e)}"
        traceback_message = traceback.format_exc()
        return {"status": 500, "message": error_message, "traceback": traceback_message}


def create_voluntario_service(voluntario: VoluntarioSchema):
    """
    Cria um novo voluntário no banco de dados.
    """
    try:
        # Cria uma nova instância do modelo VoluntarioModel
        new_voluntario = VoluntarioModel(
            nome=voluntario["nome"],
            foto=voluntario["foto"],
            email=voluntario["email"],
            telefone=voluntario["telefone"],
        )

        # Adiciona o novo voluntário ao banco de dados
        db.session.add(new_voluntario)
        db.session.commit()

        # Retorna o voluntário criado com sucesso
        return {"status": 201, "data": new_voluntario.serialize}

    except ValidationError as e:
        # Se ocorrer um erro de validação, retorna uma mensagem de erro
        return {"status": 400, "message": str(e)}

    except Exception as e:
        # Se ocorrer qualquer outro erro, retorna uma mensagem de erro com o traceback
        error_message = f"Erro ao criar um novo voluntário: {str(e)}"
        traceback_message = traceback.format_exc()
        return {"status": 500, "message": error_message, "traceback": traceback_message}


def get_voluntario_service(voluntario_id: int):
    """
    Retorna um voluntário específico do banco de dados.
    """
    try:
        # Consulta ao banco de dados para obter o voluntário com o ID fornecido
        voluntario = VoluntarioModel.query.get(voluntario_id)

        # Verifica se o voluntário existe
        if not voluntario:
            return {"status": 404, "message": "Voluntário não encontrado no banco de dados."}

        # Retorna o voluntário encontrado e o status de sucesso
        return {"status": 200, "data": voluntario.serialize}

    except Exception as e:
        # Se ocorrer qualquer erro, retorna uma mensagem de erro com o traceback
        error_message = f"Erro ao consultar o voluntário: {str(e)}"
        traceback_message = traceback.format_exc()
        return {"status": 500, "message": error_message, "traceback": traceback_message}


def update_voluntario_service(voluntario_id: int, voluntario: VoluntarioSchema):
    """
    Atualiza um voluntário específico no banco de dados.
    """
    try:
        # Consulta ao banco de dados para obter o voluntário com o ID fornecido
        voluntario_to_update = VoluntarioModel.query.get(voluntario_id)

        # Verifica se o voluntário existe
        if not voluntario_to_update:
            return {"status": 404, "message": "Voluntário não encontrado no banco de dados."}

        # Atualiza os dados do voluntário
        voluntario_to_update.nome = voluntario["nome"]
        voluntario_to_update.foto = voluntario["foto"]
        voluntario_to_update.email = voluntario["email"]
        voluntario_to_update.telefone = voluntario["telefone"]

        # Salva as alterações no banco de dados
        db.session.commit()

        # Retorna o voluntário atualizado e o status de sucesso
        return {"status": 200, "data": voluntario_to_update.serialize}

    except ValidationError as e:
        # Se ocorrer um erro de validação, retorna uma mensagem de erro
        return {"status": 400, "message": str(e)}

    except Exception as e:
        # Se ocorrer qualquer outro erro, retorna uma mensagem de erro com o traceback
        error_message = f"Erro ao atualizar o voluntário: {str(e)}"
        traceback_message = traceback.format_exc()
        return {"status": 500, "message": error_message, "traceback": traceback_message}


def delete_voluntario_service(voluntario_id: int):
    """
    Deleta um voluntário específico do banco de dados.
    """
    try:
        # Consulta ao banco de dados para obter o voluntário com o ID fornecido
        voluntario_to_delete = VoluntarioModel.query.get(voluntario_id)

        # Verifica se o voluntário existe
        if not voluntario_to_delete:
            return {"status": 404, "message": "Voluntário não encontrado no banco de dados."}

        # Deleta o voluntário do banco de dados
        db.session.delete(voluntario_to_delete)
        db.session.commit()

        # Retorna o status de sucesso
        return {"status": 204, "message": "Voluntário deletado com sucesso."}

    except Exception as e:
        # Se ocorrer qualquer erro, retorna uma mensagem de erro com o traceback
        error_message = f"Erro ao deletar o voluntário: {str(e)}"
        traceback_message = traceback.format_exc()
        return {"status": 500, "message": error_message, "traceback": traceback_message}
