import os
import json
from telegram.ext import Updater
from loguru import logger
from dotenv import load_dotenv


logger.add('logs/debug.log', level="WARNING", rotation="50 MB", compression='zip',
           enqueue=True, backtrace=True, diagnose=True)

load_dotenv()

TOKEN = os.getenv('TOKEN')

with open('utils/text_settings.json', 'r', encoding='utf-8') as file:
    SETTINGS = json.loads(file.read())

updater = Updater(TOKEN)
