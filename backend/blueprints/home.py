from flask import Blueprint, request, jsonify

home_bp = Blueprint("home", __name__)

@home_bp.route("/", methods=["GET"])
def index():
    """
    Retorna uma mensagem de boas-vindas.
    ---
    tags:
      - Home
    responses:
      200:
        description: Mensagem de boas-vindas
    """
    return jsonify({"message": "Bem-vindo(a) ao backend do Patas Felizes! Leia a documentação em /apidocs."})