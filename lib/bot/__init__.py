from dotenv import dotenv_values

config = dotenv_values('logs/.env')
TOKEN = config['TOKEN']
API_KEY = config['API_KEY']
SEARCH_ENGINE_ID = config['SEARCH_ENGINE_ID']
