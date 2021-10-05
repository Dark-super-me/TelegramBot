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
button=[]
button.append([[InlineKeyboardButton("Help", callback_data="ihelp")]])
button.append([[InlineKeyboardButton("Guide", callback_data="iguide")]])

bbutton=[]
bbutton.append([[InlineKeyboardButton("Back", callback_data="beck")]])

@bot.on_message(filters.command(['start']))
def start(bot: Client, event: Message):
    r = "Hi \nIam next generation video encoder bot!\n\nUpdates will come soon\n\nnMaintained by • @Animes_Encoded",
    text=r,
    disable_web_page_preview=True,
    parse_mode="html",
    reply_markup=InlineKeyboardMarkup(button)
    
     
      
@bot.on_callback_query()
async def callback_handlers(_, event: CallbackQuery):
    if "ihelp" in event.data:
        await event.message.edit(
            text=Translation.HELP_TEXT,
            parse_mode="html",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(bbutton))
    elif "iguide" in event.data:
            await event.message.edit(
                text=Translation.GUIDE,
                paste_made="html",
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(bbutton))
    elif "beck" in event.data:
                await event.message.edit(
                    text=Translation.START_TEXT,
                    parse_made="html",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup(button))
bot.run()
