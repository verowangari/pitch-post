import os

class Config:


    SECRET_KEY =os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://vero:1234567890@localhost:5432/elevator"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    @staticmethod
    
    def init_app(app):
        pass
    
class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    pass


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://vero:1234567890@localhost:5432/elevator"
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}