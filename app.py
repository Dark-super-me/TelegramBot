from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from config import Config
from translation import Translation 

bot = Client(
    'simp-bot',
    bot_token = Config.BOT_TOKEN,
    api_id = Config.API_ID,
    api_hash = Config.API_HASH
)
                        
