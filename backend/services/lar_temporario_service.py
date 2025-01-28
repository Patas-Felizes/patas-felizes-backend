import logging
import traceback
from marshmallow import ValidationError

from backend.external.schemas import LarTemporarioSchema
from backend.db import db
from backend.external.model import LarTemporarioModel

logger = logging.getLogger(__name__)

def get_all_lar_temporarios():
    """
    Função auxiliar para retornar todos os registros de lar temporário.
    """
    return LarTemporarioModel.query.all()

def list_lar_temporarios_service():
    """
    Retorna a lista de todos os lares temporários armazenados no banco de dados.
    """
    try:
        lares = get_all_lar_temporarios()

        if not lares:
            return {
                "status": 404,
                "message": "Nenhum lar temporário encontrado no banco de dados."
            }
        
        response_list = [lar.serialize for lar in lares]

        return {"status": 200, "data": response_list}
    except Exception as e:
        error_message = f"Erro ao listar lares temporários: {str(e)}"
        traceback_message = traceback.format_exc()
        return {"status": 500, "message": error_message, "traceback": traceback_message}


def create_lar_temporario_service(data: dict):
    """
    Cria um novo registro de lar temporário no banco de dados.
    """
    try:
        # Aqui poderíamos validar usando o LarTemporarioSchema, se desejado:
        # validated_data = LarTemporarioSchema().load(data)

        new_lar = LarTemporarioModel(
            animal_id=data["animal_id"],
            hospedeiro_id=data["hospedeiro_id"],
            periodo=data["periodo"],
            data_hospedagem=data["data_hospedagem"],
            data_cadastro=data["data_cadastro"]
        )

        db.session.add(new_lar)
        db.session.commit()

        return {"status": 201, "data": new_lar.serialize}

    except ValidationError as e:
        return {"status": 400, "message": str(e)}
    except Exception as e:
        error_message = f"Erro ao criar lar temporário: {str(e)}"
        traceback_message = traceback.format_exc()
        return {"status": 500, "message": error_message, "traceback": traceback_message}


def get_lar_temporario_service(lar_temporario_id: int):
    """
    Retorna um lar temporário específico do banco de dados.
    """
    try:
        lar = LarTemporarioModel.query.get(lar_temporario_id)

        if not lar:
            return {"status": 404, "message": "Lar temporário não encontrado."}
        
        return {"status": 200, "data": lar.serialize}
    except Exception as e:
        error_message = f"Erro ao buscar lar temporário: {str(e)}"
        traceback_message = traceback.format_exc()
        return {"status": 500, "message": error_message, "traceback": traceback_message}


def update_lar_temporario_service(lar_temporario_id: int, data: dict):
    """
    Atualiza um lar temporário específico no banco de dados.
    """
    try:
        lar_to_update = LarTemporarioModel.query.get(lar_temporario_id)

        if not lar_to_update:
            return {"status": 404, "message": "Lar temporário não encontrado."}
        
        # Atualização dos campos
        lar_to_update.animal_id = data["animal_id"]
        lar_to_update.hospedeiro_id = data["hospedeiro_id"]
        lar_to_update.periodo = data["periodo"]
        lar_to_update.data_hospedagem = data["data_hospedagem"]
        lar_to_update.data_cadastro = data["data_cadastro"]

        db.session.commit()

        return {"status": 200, "data": lar_to_update.serialize}
    
    except ValidationError as e:
        return {"status": 400, "message": str(e)}
    except Exception as e:
        error_message = f"Erro ao atualizar lar temporário: {str(e)}"
        traceback_message = traceback.format_exc()
        return {"status": 500, "message": error_message, "traceback": traceback_message}


def delete_lar_temporario_service(lar_temporario_id: int):
    """
    Deleta um lar temporário específico do banco de dados.
    """
    try:
        lar_to_delete = LarTemporarioModel.query.get(lar_temporario_id)

        if not lar_to_delete:
            return {"status": 404, "message": "Lar temporário não encontrado."}
        
        db.session.delete(lar_to_delete)
        db.session.commit()

        return {"status": 204, "message": "Lar temporário deletado com sucesso."}
    except Exception as e:
        error_message = f"Erro ao deletar lar temporário: {str(e)}"
        traceback_message = traceback.format_exc()
        return {"status": 500, "message": error_message, "traceback": traceback_message}
