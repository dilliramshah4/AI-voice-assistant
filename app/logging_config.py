import logging
from logging.handlers import RotatingFileHandler
import os

logger = logging.getLogger("voice_assistant")
logger.setLevel(logging.INFO)

handler = RotatingFileHandler(
    'app.log', maxBytes=1e6, backupCount=3
)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)