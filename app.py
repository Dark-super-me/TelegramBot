from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from config import Config
from translation import Translation 
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


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



@app.on_message(filters.command("start"))
def start(client,message):
  chat_id=message.chat_id,
  Client.send_message(
    chat_id,
    f"Hi {message.from_user.username} \n <b> I am one simple bot  made by @Bro_isDarkal \nPls click the below buttons to get a hint about this bot !\n\n By @Animes_Encoded.<b> \n",
    parse_mode="markdown",
    reply_markup=InlineKeyboardMarkup(button))
    

@bot.on_callback_query()
async def callback_handlers(_, event: CallbackQuery):
    if "ihelp" in event.data:
        await event.message.edit(
            text="Checkout The Available Commands Here \n\n Do Follow @Animes_Encoded\n\n If You Find This Bot Usefull❤️",
            parse_mode="html",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(bbutton))
    elif "iguide" in event.data:
            await event.message.edit(
                text="Right now the bot can only compress MKV formated files and the file must be Telegram Video or Telegram Document type",
                paste_made="html",
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(bbutton))
    elif "beck" in event.data:
                await event.message.edit(
                    text="Hi \nIam next generation video encoder bot!\n\nUpdates will come soon\n\nnMaintained by • @Animes_Encoded",
                    parse_made="html",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup(button))
       
          
# run the application        
bot.run()
