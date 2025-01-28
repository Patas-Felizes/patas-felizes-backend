# ENTIDADES E ATRIBUTOS - MOBILE
# ===
# Tabela Animal
# ID (chave primária)
# Nome
# Idade (composto): valor, unidade (dias, meses, anos)
# Foto
# Descrição
# Sexo (pré definido): Macho/Fêmea
# Castracao (só tem duas opções): Sim/Não
# Status (só tem 6 opções): Para adoção, Adotado, Em tratamento, Em lar temporário, Falecido, Desaparecido
# Espécie (só tem essas duas opções): Gato/Cachorro
# DataCadastro(data pega do sistema)
# ===
# Tabela Adoção
# ID (chave primária)
# AnimalID (chave estrangeira)
# AdotanteID (chave estrangeira)
# CompanhaID (chave estrangeira)
# DataDevolução
# MotivoDevolução
# DataAdocao
# DataCadastro
# ===
# Tabela Adotante
# ID (chave primária)
# Nome
# Telefone
# Email
# Moradia (composto): Estado, Cidade, Logradouro, Bairro, Numero, CEP
# ===
# Tabela Lar temporário
# ID (chave primária)
# AnimalID (chave estrangeira)
# HospedeiroID (chave estrangeira)
# Período (composto): valor, unidade (dias, meses, anos)
# DataHospedagem
# DataCadastro
# ===
# Tabela Hospedeiro
# ID (chave primária)
# Nome
# Telefone
# Email
# Moradia: Estado, Cidade, Logradouro, Bairro, Numero, CEP
# ===
# Tabela Apadrinhamento
# ID (chave primária)
# AnimalID (chave estrangeira)
# NomeApadrinhador (chave estrangeira)
# Valor
# Regularidade (pré definido): quinzenalmente, mensalmente, semestralmente
# ===
# Tabela Procedimento
# ID (chave primária)
# Tipo
# Descricao
# Valor
# DataProcedimento
# AnimalID (chave estrangeira)
# VoluntarioID (chave estrangeira)
# DespesaID (chave estrangeira)
# ===
# Tabela Campanha
# ID (chave primária)
# Nome
# Tipo
# DataInício
# DataTérmino
# Descrição
# Local
# ===
# Tabela Doação
# ID (chave primária)
# Doador
# Valor
# DataDoação
# AnimalID (chave estrangeira): (se tiver pet associado)
# CompanhaID (chave estrangeira)
# EstoqueID
# Comprovante
# Tabela Despesa
# ===
# ID (chave primária)
# Valor
# DataDespesa
# Tipo
# AnimalID (chave estrangeira): se tiver pet associado
# ProcedimentoID (chave estrangeira): se tiver procedimento associado
# Comprovante
# Tabela Estoque
# ===
# ID (chave primária)
# Categoria
# TipoItem
# Descrição
# EspecieAnimal
# Quantidade (composto): valor, unidade  
# QuantidadeTotal
# ===
# Tabela Tarefa
# ID (chave primária)
# Tipo
# Descrição
# DataTarefa
# VoluntárioID (chave estrangeira)
# AnimalID (chave estrangeira): se tiver pet associado
# ===
# Tabela Voluntário 
# ID (chave primária)
# Nome
# Foto
# Email
# Telefone

import secure
from flasgger import Swagger
from flask import Flask

from backend.blueprints.animal import animal_bp
from backend.blueprints.adocao import adocao_bp
from backend.blueprints.adotante import adotante_bp
from backend.blueprints.lar_temporario import lar_temporario_bp
from backend.blueprints.hospedeiro import hospedeiro_bp
from backend.blueprints.apadrinhamento import apadrinhamento_bp
from backend.blueprints.procedimento import procedimento_bp
from backend.blueprints.campanha import campanha_bp
from backend.blueprints.doacao import doacao_bp
from backend.blueprints.despesa import despesa_bp
from backend.blueprints.estoque import estoque_bp
from backend.blueprints.tarefa import tarefa_bp
from backend.blueprints.voluntario import voluntario_bp
from backend.blueprints.auth import auth
from backend.config import get_config
from backend.db import db
from backend.extention import cors, migrate
from backend.utils.logging import configure_logging


def create_app():
    app = Flask(__name__)

    # Load configurations
    config, env = get_config()
    app.config.from_object(config)

    # Initialize the extensions
    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app, supports_credentials="true", resources={r"*": {"origins": "*"}})

    # Registering blueprints
    app.register_blueprint(animal_bp)
    app.register_blueprint(adocao_bp)
    app.register_blueprint(adotante_bp)
    app.register_blueprint(lar_temporario_bp)
    app.register_blueprint(hospedeiro_bp)
    app.register_blueprint(apadrinhamento_bp)
    app.register_blueprint(procedimento_bp)
    app.register_blueprint(campanha_bp)
    app.register_blueprint(doacao_bp)
    app.register_blueprint(despesa_bp)
    app.register_blueprint(estoque_bp)
    app.register_blueprint(tarefa_bp)
    app.register_blueprint(voluntario_bp)
    app.register_blueprint(auth)

    # Logging configuration
    configure_logging(app)

    SWAGGER_TEMPLATE = {
        "securityDefinitions": {
            "APIKeyHeader": {"type": "apiKey", "name": "Authorization", "in": "header"}
        }
    }
    swagger = Swagger(app, template=SWAGGER_TEMPLATE)

    # change STS Security
    # Forces the browser to communicate with the website only via HTTPS, even if the user types the address with HTTP
    hsts_value = (
        secure.StrictTransportSecurity().include_subdomains().preload().max_age(2592000)
    )

    # add Referrer Policy
    # Controls the amount of information the browser sends in the Referer header when a link is clicked.
    # The Referer indicates where the user came from, and this information can be used to track users.
    # By default, the header will not be sent
    referrer_value = secure.ReferrerPolicy().no_referrer()

    # add X frame options
    # Determines whether a page can be embedded in an iframe.
    # By default, only on same-origin pages.
    xfo_value = secure.XFrameOptions().sameorigin()

    # add xxss protection
    # Instructs the browser to enable XSS (Cross-Site Scripting) protection.
    # This protection helps prevent malicious code from being injected into a web page.
    xxss_value = secure.XXSSProtection().set("1")

    secure_headers = secure.Secure(
        hsts=hsts_value, referrer=referrer_value, xfo=xfo_value, xxp=xxss_value
    )

    # setting to use secure headers in all requests
    @app.after_request
    def set_secure_headers(response):
        secure_headers.framework.flask(response)

        # add custom headers
        # These are security policies that restrict how a document can be embedded or open pop-ups from other websites.
        # By default, the site need to be in same origin.
        response.headers.set("Cross-Origin-Opener-Policy", "same-origin")
        response.headers.set("Cross-Origin-Embedder-Policy", "require-corp")

        # Allows you to specify which types of resources can be accessed by other websites.
        # This helps prevent CSRF (Cross-Site Request Forgery) attacks.
        response.headers.set("Cross-Origin-Resource-Policy", "same-origin")

        return response

    return app
