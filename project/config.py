import base64
import os
from enum import Enum
from pathlib import Path
from typing import Type, List

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()


class BaseConfig:
    SECRET_KEY = os.getenv('SECRET_KEY', 'you-will-never-guess')
    ALGORITHM = 'HS256'
    JSON_AS_ASCII = False

    ITEMS_PER_PAGE = 12

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    TOKEN_EXPIRE_MINUTES = 15
    TOKEN_EXPIRE_DAYS = 130

    PWD_HASH_SALT = base64.b64decode("salt")
    PWD_HASH_ITERATIONS = 100_000

    RESTX_JSON = {
        'ensure_ascii': False,
    }


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + BASE_DIR.joinpath('project.db').as_posix()


class ProductionConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "postgresql://{username}:{password}@{host}:{port}/{db_name}".format(
        username=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host=os.getenv("POSTGRES_HOST", '127.0.0.1'),
        port=int(os.getenv("POSTGRES_PORT", 5432)),
        db_name=os.getenv("POSTGRES_DB")
    )
    SWAGGER_SUPPORTED_SUBMIT_METHODS: List[str] = []


class Config(Enum):
    development = DevelopmentConfig
    testing = TestingConfig
    production = ProductionConfig


def get_config(config_name: str):
    return getattr(Config, config_name, Config.production).value
