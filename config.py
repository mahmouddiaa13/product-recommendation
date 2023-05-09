import os

from dotenv import load_dotenv

load_dotenv()
WORKING_ENV = os.getenv("WORKING_ENV")


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    API_VERSION = os.getenv("DEV_API_VERSION")
    MODEL_FILE_PATH = os.getenv("MODEL_FILE_PATH")


class TestingConfig(Config):
    TESTING = True
    API_VERSION = os.getenv("TEST_API_VERSION")
    model_file_path = os.getenv("model_file_path")


class ProductionConfig(Config):
    pass


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig
}
