from pyrogram import Client, filters
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultArticle, InputTextMessageContent)
from config import Config

bot = Client(
    'simp-bot',
    bot_token = Config.BOT_TOKEN,
    api_id = Config.API_ID,
    api_hash = Config.API_HASH
)
# let's make some simple filters...

@bot.on_message(filters.command(['start']))
def start(client, message):
  r = f"Hi **{message.from_user.username}**\n\nThis is one simple bot\nThis is in beta now.\n/help for more details\n**Dev- @Bro_isDarkal**"
  message.reply_text(
    text=r,
    quote=False,
    reply_markup=InlineKeyboardMarkup(
      [
        [
          InlineKeyboardButton('Source Code 🤤', url='https://t.me/shity_man')
          ]
        ]
      )
    )
  
@bot.on_message(filters.command(['help']))
def help(client, message):
  message.reply_text("No help modules set right now !!\n\nSoon , new update will come!")
    
    
# run the bot
bot.run()
