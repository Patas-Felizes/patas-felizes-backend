import logging
import traceback
from marshmallow import ValidationError

from backend.external.schemas import AnimalSchema
from backend.db import db
from backend.external.model import (
    AnimalModel,
)

from backend.utils.pagination import build_pagination

# Create logger for this module
logger = logging.getLogger(__name__)


def get_all_animals():
    # Consulta ao banco de dados para obter todos os animais
    animal_list = AnimalModel.query.all()

    return animal_list

def list_animals_service():
    """
    Retorna a lista de todos os animais armazenados no banco de dados.
    """
    try:
        logger.info("Listando animais...")
        # Consulta ao banco de dados para obter todos os animais
        animal_list = get_all_animals()

        # Verifica se a lista está vazia
        if not animal_list:
            logger.error("Nenhum animal encontrado no banco de dados.")
            return {
                "status": 404,
                "message": "Nenhum animal encontrado no banco de dados.",
            }

        # Serializa os animais
        response_list = [animal.serialize for animal in animal_list]

        # Retorna os dados serializados e o status de sucesso
        logger.info("Animais listados com sucesso.")
        return {"status": 200, "data": response_list}

    except Exception as e:
        # Se ocorrer qualquer erro, retorna um dicionário com o erro e o traceback
        error_message = f"Erro ao consultar ou listar animais: {str(e)}"
        traceback_message = traceback.format_exc()
        logger.error(error_message)
        return {"status": 500, "message": error_message, "traceback": traceback_message}
    
def create_animal_service(animal: AnimalSchema):
    """
    Cria um novo animal no banco de dados.
    """
    try:
        logger.info("Criando um novo animal...")
        # Cria uma nova instância do modelo AnimalModel
        new_animal = AnimalModel(
            nome=animal["nome"],
            idade=animal["idade"],
            foto=animal["foto"],
            descricao=animal["descricao"],
            sexo=animal["sexo"],
            castracao=animal["castracao"],
            status=animal["status"],
            especie=animal["especie"],
            data_cadastro=animal["data_cadastro"],
        )

        # Adiciona o novo animal ao banco de dados
        db.session.add(new_animal)
        db.session.commit()

        # Retorna o animal criado com sucesso
        logger.info("Novo animal criado com sucesso.")
        return {"status": 201, "data": new_animal.serialize}

    except ValidationError as e:
        # Se ocorrer um erro de validação, retorna uma mensagem de erro
        logger.error(f"Erro de validação ao criar um novo animal: {str(e)}")
        return {"status": 400, "message": str(e)}

    except Exception as e:
        # Se ocorrer qualquer outro erro, retorna uma mensagem de erro com o traceback
        error_message = f"Erro ao criar um novo animal: {str(e)}"
        traceback_message = traceback.format_exc()
        logger.error(error_message)
        return {"status": 500, "message": error_message, "traceback": traceback_message}
    
def get_animal_service(animal_id: int):
    """
    Retorna um animal específico do banco de dados.
    """
    try:
        logger.info(f"Consultando animal com ID {animal_id}...")
        # Consulta ao banco de dados para obter o animal com o ID fornecido
        animal = AnimalModel.query.get(animal_id)

        # Verifica se o animal existe
        if not animal:
            logger.error("Animal não encontrado no banco de dados.")
            return {"status": 404, "message": "Animal não encontrado no banco de dados."}

        # Retorna o animal encontrado e o status de sucesso
        logger.info("Animal encontrado com sucesso.")
        return {"status": 200, "data": animal.serialize}

    except Exception as e:
        # Se ocorrer qualquer erro, retorna uma mensagem de erro com o traceback
        error_message = f"Erro ao consultar o animal: {str(e)}"
        traceback_message = traceback.format_exc()
        logger.error(error_message)
        return {"status": 500, "message": error_message, "traceback": traceback_message}
    
def update_animal_service(animal_id: int, animal: AnimalSchema):
    """
    Atualiza um animal específico no banco de dados.
    """
    try:
        logger.info(f"Atualizando animal com ID {animal_id}...")
        # Consulta ao banco de dados para obter o animal com o ID fornecido
        animal_to_update = AnimalModel.query.get(animal_id)

        # Verifica se o animal existe
        if not animal_to_update:
            logger.error("Animal não encontrado no banco de dados.")
            return {"status": 404, "message": "Animal não encontrado no banco de dados."}

        # Atualiza os dados do animal
        animal_to_update.nome = animal["nome"]
        animal_to_update.idade = animal["idade"]
        animal_to_update.foto = animal["foto"]
        animal_to_update.descricao = animal["descricao"]
        animal_to_update.sexo = animal["sexo"]
        animal_to_update.castracao = animal["castracao"]
        animal_to_update.status = animal["status"]
        animal_to_update.especie = animal["especie"]
        animal_to_update.data_cadastro = animal["data_cadastro"]

        # Salva as alterações no banco de dados
        db.session.commit()

        # Retorna o animal atualizado e o status de sucesso
        logger.info("Animal atualizado com sucesso.")
        return {"status": 200, "data": animal_to_update.serialize}

    except ValidationError as e:
        # Se ocorrer um erro de validação, retorna uma mensagem de erro
        logger.error(f"Erro de validação ao atualizar o animal: {str(e)}")
        return {"status": 400, "message": str(e)}

    except Exception as e:
        # Se ocorrer qualquer outro erro, retorna uma mensagem de erro com o traceback
        error_message = f"Erro ao atualizar o animal: {str(e)}"
        traceback_message = traceback.format_exc()
        logger.error(error_message)
        return {"status": 500, "message": error_message, "traceback": traceback_message}
    
def delete_animal_service(animal_id: int):
    """
    Deleta um animal específico do banco de dados.
    """
    try:
        logger.info(f"Deletando animal com ID {animal_id}...")
        # Consulta ao banco de dados para obter o animal com o ID fornecido
        animal_to_delete = AnimalModel.query.get(animal_id)

        # Verifica se o animal existe
        if not animal_to_delete:
            logger.error("Animal não encontrado no banco de dados.")
            return {"status": 404, "message": "Animal não encontrado no banco de dados."}

        # Deleta o animal do banco de dados
        db.session.delete(animal_to_delete)
        db.session.commit()

        # Retorna o status de sucesso
        logger.info("Animal deletado com sucesso.")
        return {"status": 204, "message": "Animal deletado com sucesso."}

    except Exception as e:
        # Se ocorrer qualquer erro, retorna uma mensagem de erro com o traceback
        error_message = f"Erro ao deletar o animal: {str(e)}"
        traceback_message = traceback.format_exc()
        logger.error(error_message)
        return {"status": 500, "message": error_message, "traceback": traceback_message}