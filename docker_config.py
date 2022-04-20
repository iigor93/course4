""" файл с конфиругацией """


class Config(object):
    """Настройка приложения Flask"""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "postgresql://postgresql_user:enigma42@localhost:5432/lesson19"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_TO_ASCII = False


# Данные для генерации Hash для пароля
PWD_HASH_SALT = b'Djk7&FFLEoDuf*o9(*'
PWD_HASH_ITERATIONS = 100_000


# Данные для генерации token
ALGO = 'HS256'
SECRET = 's3cR$eT_WrD'
