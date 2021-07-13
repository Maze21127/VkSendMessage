from os import environ
from dotenv import load_dotenv

load_dotenv('.env')
LOGIN = environ['LOGIN']
PASSWORD = environ['PASSWORD']
TT_KEY = environ['TT_KEY']
PYOWM_KEY = environ['PYOWM_KEY']
YANDEX_API_KEY = environ['YANDEX_API_KEY']
EMAIL = environ['EMAIL']
EMAIL_PASSWORD = environ['EMAIL_PASSWORD']
