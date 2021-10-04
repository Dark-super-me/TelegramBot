from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from config import Config
from translation import Translation 

Encoder = Client(
    'simp-bot',
    bot_token = Config.BOT_TOKEN,
    api_id = Config.API_ID,
    api_hash = Config.API_HASH
)
HELP_BUTTON = InlineKeyboardMarkup(
    [[
        InlineKeyboardButton ("♨️ HELP", callback_data="ihelp"),
        InlineKeyboardButton ("📋 GUIDE", callback_data="iguide")
    ]]
)   

GUIDE_BUTTON = InlineKeyboardMarkup(
    [[
        InlineKeyboardButton ("Back", callback_data="beck")
    ]]
)
@Encoder.on_message(filters.command(['start']))
def start(client, message):
    text=Translation.START_TEXT,
    quote=False,
    reply_markup=HELP_BUTTON  
    
     
      
@Encoder.on_callback_query()
async def cb_handler(client: Encoder , query: CallbackQuery):
    data = query.data
    if data == "ihelp":
        try:
            await query.message.edit_text(
                text=Translation.HELP_TEXT,
                quote=False,
                reply_markup=GUIDE_BUTTON
   # elif data == "iguide":
       # try:
           # await query.message.edit_text(
                #text=Translation.GUIDE,
               # quote=False,
              #  reply_markup=GUIDE_BUTTON
    
   # elif data == "beck":
     #   try:
         #   await query.message.edit_text(
         #       text=Translation.START_TEXT,
               # quote=False,
               # reply_markup=GUIDE_BUTTON
       # except:
          #  pass
        
           
 Encoder.run()         
 # fine            
