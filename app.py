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
    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('♨️ HELP', callback_data="ihelp"),InlineKeyboardButton('📋 GUIDE', callback_data="iguide")]]))
           
  
@bot.on_callback_query()
async def cb_handler(client: bot , query: CallbackQuery);
    data = query.data
    if data == "ihelp":
        try:
            
            
            await query.message.edit_text(
                
                text=Translation.HELP_TEXT,
            quote=False,
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('📋 GUIDE', callback_data="iguide"),InlineKeyboardButton('Back', callback_data="beck")]]))
    elif data == "iguide":
        await query.message.edit_text(
            text=Translation.GUIDE,
            quote=False,
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('Back', callback_data="beck")]]))
    elif data == "beck":
        await query.message.edit_text(
            text=Translation.START_TEXT,
            quote=False,
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('♨️ HELP', callback_data="ihelp"),InlineKeyboardButton('📋 GUIDE', callback_data="iguide")]]))
           
            
            
            
    
        
        
    
            
           
            
            
           
                
        
    

