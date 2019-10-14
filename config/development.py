from config  import Config

class Development(Config):
    ENV_TYPE = "Dev"

    DB_NAME = 'praksa_baza'
    DB_USER = "marko"
    DB_PASSWD = "123456"
    DB_HOST = "127.0.0.1"
    DB_PORT = 5432

    SQLALCHEMY_DATABASE_URI =\
    f'postgresql+psycopg2://'\
    f'{DB_USER}:{DB_PASSWD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'