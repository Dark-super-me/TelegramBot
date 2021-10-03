from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from config import Config
from helper import OpenSettings 
bot = Client(
    'simp-bot',
    bot_token = Config.BOT_TOKEN,
    api_id = Config.API_ID,
    api_hash = Config.API_HASH
)
# let us defines some events 
# oof the callback .
@bot.on_callback_query()
async def callback_handlers(bot: Client, cb: CallbackQuery):
    if "closeme" in cb.data:
        await cb.message.delete(True)
    elif "opensettings" in cb.data:
        await OpenSettings(cb.message, user_id=cb.from_user.id)
        
# Import OpenSettings ...
                                         

@bot.on_message(filters.command(['start']))
def start(client, message):
  r = f"`Hello {message.from_user.username} \n\nThis is a Telegram  Bot. \n\nI am still in a beta mode as I was built by my dev recently\n\n/help for more details.\n\nChannel : @Animes_Encoded`"
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
    
@bot.on_callback_query()
                                         
                                         
                                         
# run the bot
                                         
                                         
                                         
                                         
                                         
                                         
                                         
                                         
                                         
                                         
                                         
                                         
                                         
                                         
                                         
                                         
                                         
                                         
                                         
                                         
                                         
                                         
                                         
                                         
bot.run()
