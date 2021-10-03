from pyrogram import Client, filters
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultArticle, InputTextMessageContent)
from config import Config

bot = Client(
    'simp-bot',
    bot_token = Config.BOT_TOKEN,
    api_id = Config.API_ID,
    api_hash = Config.API_HASH
)
# let us defines some events 
async def help(event):
    await message.reply_text(
        "The Bot isnt fully completed yet by the Owner\n\nPlease be patient until further notice\n\nJoin @Animes_Encoded"
    )
async def thelp(event):
    oof = f"`Hi {message.from_user.username} \n\nThe Bot isnt fully developed by the owner.\n\nPlease be patient until further notice"
    message.reply_text(
        text=oof
        quote=False,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('Back', callback
        
    
    
# let's make some simple filters...

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
    
    
# run the bot
bot.run()
