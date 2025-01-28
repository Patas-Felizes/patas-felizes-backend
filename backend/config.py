import os

from dotenv import load_dotenv

load_dotenv()


def get_config():
    map_config = {
        "local": LocalConfig(),
        "development": DevelopmentConfig(),
        #'homolog': HomologationConfig(),
        #'production': ProductionConfig(),
    }
    # Os ambientes com o prefixo `migration-` devem rodar com o usuário de administração

    env = os.getenv("FLASK_ENV", "local").lower()
    config = map_config[env]
    return config, env


class DefaultConfig:
    # Flask Configuration
    APP_NAME = os.environ.get("APP_NAME")
    API_VERSION = os.environ.get("API_VERSION")

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SHOW_SQLALCHEMY_LOG_MESSAGES = False

    SWAGGER = {
        "swagger": "2.0",
        "uiversion": 3,
        "info": {"title": APP_NAME, "version": API_VERSION},
    }

    # Configuration to JWT
    SECRET_KEY = os.environ.get("SECRET_KEY")
    AUDIENCE = os.environ.get("AUDIENCE")
    
    DATABASE_URL = os.getenv("DATABASE_URL")


class LocalConfig(DefaultConfig):
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = DefaultConfig.DATABASE_URL


class DevelopmentConfig(DefaultConfig):
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = DefaultConfig.DATABASE_URL


class HomologationConfig(DefaultConfig):
    DEBUG = False

    SQLALCHEMY_DATABASE_URI = DefaultConfig.DATABASE_URL


class ProductionConfig(DefaultConfig):
    DEBUG = False

    SQLALCHEMY_DATABASE_URI = DefaultConfig.DATABASE_URL
