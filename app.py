from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from config import Config
from translation import Translation 
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

bot=Client(
  'roof',
  bot_token=Config.BOT_TOKEN,
  api_id=Config.API_ID,
  api_hash=Config.API_HASH
)
  

button=[]
button.append([InlineKeyboardButton("Help", callback_data="ihelp")])
button.append([InlineKeyboardButton("Guide", callback_data="iguide")])

bbutton=[]
bbutton.append([InlineKeyboardButton("Back", callback_data="beck")])
# python (c) list 


@bot.on_message(filters.command("start"))
async def start(client,message):
  await client.send_message(
    message.chat.id,
    text=f"Hi {message.from_user.username} \n <b> I am one simple bot  made by @Bro_isDarkal \nPls click the below buttons to get a hint about this bot !\n\n By @Animes_Encoded.<b> \n",
    reply_markup=InlineKeyboardMarkup(button))
   
# callback data is below .....
@bot.on_callback_query()
async def callback_handlers(_, event: CallbackQuery):
    if "ihelp" in event.data:
       await event.message.edit_text(
         
           text="Checkout The Available Commands Here \n\n Do Follow @Animes_Encoded\n\n If You Find This Bot Usefull❤️",
           reply_markup=InlineKeyboardMarkup(bbutton))
    elif "iguide" in event.data:
       await event.message.edit(
         
         text="Right now the bot can only compress MKV formated files and the file must be Telegram Video or Telegram Document type",
         reply_markup=InlineKeyboardMarkup(bbutton))
    elif "beck" in event.data:
       await event.message.edit(
         
          text="Hi \nIam next generation video encoder bot!\n\nUpdates will come soon\n\nnMaintained by • @Animes_Encoded",
          reply_markup=InlineKeyboardMarkup(button))
        
           
       
          
# run the application        
bot.run()
