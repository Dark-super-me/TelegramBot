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
  
    
@bot.on_message(filters.command(['start']))
def start(client, message):
    text=Translation.START_TEXT,
    quote=False,
    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('HELP', callback_data="ihelp")],InlineKeyboardButton('GUIDE', callback_data="iguide")]]))
    
           
         
            
@bot.on_callback_query()
async def cb_handler(client: bot , query: CallbackQuery);
    data = query.data
    if data == "ihelp":
        
        
    
            
           
            
            
           
                
        
    

