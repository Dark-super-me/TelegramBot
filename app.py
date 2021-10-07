from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from config import Config

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

START_TEXT = """ <b>Hi , \nI'm a next generation video encoder bot!</b> \n
<b>Bot Maintained By: @Animes_Encoded</b> \n 
"""
   

HELP_TEXT = """Checkout The Available Commands Here \n\n Do Follow @Animes_Encoded\n\n If You Find This Bot Usefull❤️"""

GUIDE = """<b>Right now the bot can only compress MKV formated files
and the file must be Telegram Video or Telegram Document type
to learn more specifically, use this /help <setting name>
for example /help crf\n\nhelp is available for:\nCRF\nVBR\nCoDec<b> \n"""
CRF = """
<b>CRF(Constant Rate Factor)<b>
it is the main quality and size controlling option
since the Rate Factor is Constant, the
video will have constant quality throughout
the whole duration.
more size means more quality but depending on
other settings we used we might decrease the  output size.
bit rate types
   variable
   constant
The two ways of having a variable BitRate are
inputting Average BitRate or ConstantRateFactor(CRF)
for a person whose aim is having lower size video file,
then CRF is the best choiceOn Animes_Encoded we have been using crf of 24-35
The highest the number the lowest size and quality and vice versa
to learn more, google search and also you can use
a software called MediaInfo to check the crf used
when encoding a video file.
"""
VBR = """
<b>vbr(Variable Bit Rate)<b>
it is one of the settings we use to set the
audio quality. so depending on the profile used
The BitRate differs for each level
it has 5 levels. 1 is the lowest BitRate and 5 is the highest
"""

CoDec = """
<b>CoDec(Coder-Decoder)<b>
codec is the thing that convert data from digital into Analogue
or vice versa
 when we play video we can say we are Decoding or
we are using a decoder, and when we are Recording a video through
our camera, we can say we are Encoding or we are using coder
when we try to convert a file structure from one codec to another
we are TransCoding, this time we are both decoding and encoding.
when we are trying to change aspectRatio or resolution or any other property
without changing the codec, we can say we are Re-Encoding,
also we are both decoding and encoding this time too.
"""

  
guide_b=[]
guide_b.append([InlineKeyboardButton("CRF", callback_data="icrf")])
guide_b.append([InlineKeyboardButton("CODEC", callback_data="icodec")])
guide_b.append([InlineKeyboardButton("VBR", callback_data="ivbr")])

button=[]
button.append([InlineKeyboardButton("♨️ HELP ", callback_data="ihelp")])
button.append([InlineKeyboardButton("📋 GUIDE ", callback_data="iguide")])

bbutton=[]
bbutton.append([InlineKeyboardButton("↗️ BACK ", callback_data="beck")])
# python (c) list 


@bot.on_message(filters.command("start"))
async def start(client,message):
  await client.send_message(
    message.chat.id,
    text=START_TEXT,
    reply_markup=InlineKeyboardMarkup(button))
   
# callback data is below .....
@bot.on_callback_query()
async def callback_handlers(_, event: CallbackQuery):
    if "ihelp" in event.data:
       await event.message.edit_text(
         text=HELP_TEXT,
         reply_markup=InlineKeyboardMarkup(bbutton))
         
           
    elif "iguide" in event.data:
       await event.message.edit(
         text=GUIDE,
         reply_markup=InlineKeyboardMarkup(guide_b))
         
         
    elif "beck" in event.data:
       await event.message.edit(
         text=START_TEXT,
         reply_markup=InlineKeyboardMarkup(button))
         
          
           
       
          
# run the application        
bot.run()
