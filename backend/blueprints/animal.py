from flask import Blueprint, request, jsonify
import base64
from backend.services.animal_service import (
    list_animals_service,
    get_animal_service,
    create_animal_service,
    update_animal_service,
    delete_animal_service
)

animal_bp = Blueprint("animal", __name__, url_prefix="/animals")

def decode_foto(base64_str):
    try:
        return base64.b64decode(base64_str)
    except Exception as e:
        raise ValueError(f"Invalid base64 string: {e}")

def prepare_response_data(animal):
    """
    Prepara os dados do animal para retornar pela API,
    convertendo a foto em formato de base64 string.
    """
    if animal is None:
        return None
        
    # Se for uma lista de animais
    if isinstance(animal, list):
        return [prepare_response_data(a) for a in animal]
    
    # Se for um único animal
    data = dict(animal)
    
    # Converter a foto de bytes para uma string base64
    if 'foto' in data and data['foto']:
        if isinstance(data['foto'], (bytes, bytearray)):
            data['foto'] = base64.b64encode(data['foto']).decode('utf-8')
    else:
        # Se não tiver foto ou foto vazia, inicializa como string vazia
        data['foto'] = ""
        
    return data

@animal_bp.route("/", methods=["GET"])
def list_animals():
    """
    Lista todos os animais armazenados no banco de dados.
    """
    response = list_animals_service()
    if response["status"] == 200:
        # Preparar os dados antes de enviar
        prepared_data = prepare_response_data(response["data"])
        return jsonify(prepared_data)
    return jsonify({"message": response["message"]}), response["status"]

@animal_bp.route("/<int:animal_id>", methods=["GET"])
def get_animal(animal_id):
    """
    Retorna um animal específico do banco de dados.
    """
    response = get_animal_service(animal_id)
    if response["status"] == 200:
        # Preparar os dados antes de enviar
        prepared_data = prepare_response_data(response["data"])
        return jsonify(prepared_data)
    return jsonify({"message": response["message"]}), response["status"]

@animal_bp.route("/", methods=["POST"])
def create_animal():
    """
    Cria um novo animal no banco de dados.
    """
    try:
        # Get the JSON data from the request
        animal_data = request.get_json()
        
        # Validate and convert foto if present
        if 'foto' in animal_data:
            try:
                animal_data['foto'] = decode_foto(animal_data['foto'])
            except ValueError as ve:
                return jsonify({"message": str(ve)}), 400
        
        response = create_animal_service(animal_data)
        if response["status"] == 201:
            # Preparar os dados antes de enviar na resposta
            prepared_data = prepare_response_data(response["data"])
            return jsonify(prepared_data), response["status"]
        return jsonify({"message": response["message"]}), response["status"]
    
    except Exception as e:
        # Log the full error for debugging
        import traceback
        traceback.print_exc()
        return jsonify({"message": f"Erro interno: {str(e)}"}), 500

@animal_bp.route("/<int:animal_id>", methods=["PUT"])
def update_animal(animal_id):
    """
    Atualiza um animal específico no banco de dados.
    """
    try:
        # Get the JSON data from the request
        animal_data = request.get_json()
        
        # Validate and convert foto if present
        if 'foto' in animal_data:
            try:
                animal_data['foto'] = decode_foto(animal_data['foto'])
            except ValueError as ve:
                return jsonify({"message": str(ve)}), 400
        
        response = update_animal_service(animal_id, animal_data)
        if response["status"] == 200:
            # Preparar os dados antes de enviar
            prepared_data = prepare_response_data(response["data"])
            return jsonify(prepared_data)
        return jsonify({"message": response["message"]}), response["status"]
    
    except Exception as e:
        # Log the full error for debugging
        import traceback
        traceback.print_exc()
        return jsonify({"message": f"Erro interno: {str(e)}"}), 500

@animal_bp.route("/<int:animal_id>", methods=["DELETE"])
def delete_animal(animal_id):
    """
    Deleta um animal específico do banco de dados.
    """
    response = delete_animal_service(animal_id)
    return jsonify({"message": response["message"]}), response["status"]