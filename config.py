import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


import os 

class Config:
  BOT_TOKEN = os.environ.get("BOT_TOKEN")
  API_ID = int(os.environ.get("API_ID"))
  API_HASH = os.environ.get("API_HASH")

