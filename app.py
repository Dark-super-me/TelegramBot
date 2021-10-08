from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from config import Config
import subprocess
from threading import Thread

from pykeyboard import InlineKeyboard

import time
import asyncio
import re
from os import mkdir, system

import ffmpeg


import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

app=Client(
  'roof',
  bot_token=Config.BOT_TOKEN,
  api_id=Config.API_ID,
  api_hash=Config.API_HASH
)

START_TEXT = """ <b>Hi , \nI'm a next generation video encoder bot!</b> \n
<b>Bot Maintained By: @Animes_Encoded</b> \n 
"""
   

HELP_TEXT = """This <b>bot</b> can encode videos in multiple qualities\n\nQueue Feature isnt added for now due to some reasons</b>\n\nFor converting videos reply video file by /convert\n\nJoin @Animes_Encoded \n\n❤ Made by love """

GUIDE = """<b>Right now the bot can only compress MKV formated files
and the file must be Telegram Video or Telegram Document type
to learn more specifically, use this /help <setting name>
for example /help crf\n\nhelp is available for:\nCRF\nVBR\nCoDec</b> \n"""
CRF = """
<b>CRF(Constant Rate Factor)</b>
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
<b>vbr(Variable Bit Rate)</b>
it is one of the settings we use to set the
audio quality. so depending on the profile used
The BitRate differs for each level
it has 5 levels. 1 is the lowest BitRate and 5 is the highest
"""

CoDec = """
<b>CoDec(Coder-Decoder)</b>
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
guide_b.append([InlineKeyboardButton("🗳 CRF", callback_data="icrf")])
guide_b.append([InlineKeyboardButton("🗳 CODEC", callback_data="icodec")])
guide_b.append([InlineKeyboardButton("🗳 VBR", callback_data="ivbr")])
guide_b.append([InlineKeyboardButton("↗️ BACK ", callback_data="beck")])

button=[]
button.append([InlineKeyboardButton("♨️ HELP ", callback_data="ihelp")])
button.append([InlineKeyboardButton("💿 FFMPEG DOCS ", callback_data="iguide")])

bbutton=[]
bbutton.append([InlineKeyboardButton("↗️ BACK ", callback_data="beck")])
# python (c) list 


@app.on_message(filters.command("start"))
async def start(client,message):
  await client.send_message(
    message.chat.id,
    text=START_TEXT,
    reply_markup=InlineKeyboardMarkup(button))
   
# callback data is below .....
@app.on_callback_query()
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
    elif "icrf" in event.data:
      await event.message.edit(
        text=CRF,
        reply_markup=InlineKeyboardMarkup(guide_b))
    elif "ivbr" in event.data:
       await event.message.edit(
         text=VBR,
         reply_markup=InlineKeyboardMarkup(guide_b))
    elif "icodec" in event.data:
      await event.message.edit(
        text=CoDec,
        reply_markup=InlineKeyboardMarkup(guide_b))
  
      
         
# let's add the basic ffmpeg settings 
# if u find this repo public dont kang it , I (c) owner of @Animes_Encoded gives  copyright to the below content as it contains my ffmpeg knowledge and some noob python works 
# (c) @Animes_Encoded
class Convert:
    def __init__(self, quality, file, outfile):
        if quality == "Compressed":
            self._cmd = 'ffmpeg -i "{}" -c:v libx265 -crf 32.4  -preset veryfast -c:a libopus -ab 30k -pix_fmt yuv420p -movflags +faststart -s 856x480  "{}" -y'.format(file, outfile)
        else:
            self._cmd = 'ffmpeg -i "{}" -vf scale="trunc(oh*a/2)*2:{}" -c:v libx265 -crf 32 -preset veryfast -c:a libopus -ab 40k -pix_fmt yuv420p -movflags +faststart "{}" -y'.format(
                file, quality, outfile)
        self._done = False
        self.progress = None
        self._fname = file.split("/")[-1]
        self._fpath = file

    def startasdaemon(self):
        process = subprocess.Popen(self._cmd, shell=True, errors="replace", stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT)
        while not self._done:
            realtime_output = process.stdout.readline()
            if realtime_output == '' and process.poll() is not None:
                self._done = True
                self.progress = "Completed Encoding"

                break
            if realtime_output:
                try:
                    prog = re.findall(r"(\d*%\|[\w\W]*\d*/\d+)", realtime_output.strip())[0].split(" ")
                except:
                    prog = []
                if prog:
                    self.progress = "Encoding File {} \n{}\nFrames: {}".format(self._fname, "".join(prog[:-1]),
                                                                               prog[-1])

    def start(self):
        t = Thread(target=self.startasdaemon)
        t.start()


async def format_bytes(size):
    power = 2 ** 10
    n = 0
    power_labels = {0: '', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + power_labels[n] + 'B'


async def progressbar(current, total, query, startedon, dlorup):
    diff = time.time() - startedon
    current_percent = str(round((current / total) * 100, 2))
    speed = current / diff
    current_formatted = await format_bytes(current)
    total_formatted = await format_bytes(total)
    speed_formatted = await format_bytes(speed)
    if int(diff)%5==0:
        await query.edit_text(
        "{} The File\nProgress: {}/{}  {}\nPercentage: {}".format(
            dlorup, current_formatted, total_formatted, speed_formatted + "/s", current_percent+"%")
    )


async def upload2tg(query, fpath):
    start = time.time()
    fname = fpath.split("/")[-1]
    await query.message.edit("Starting the upload of file ``" + fname + "``")
    await query.message.reply_video(fpath,
                                    progress=progressbar,
                                    progress_args=(query, start, "Uploading")

                                    )

    dirname = '/'.join(fpath.split("/")[:-1])
    system("rm -rf "+dirname)


@app.on_callback_query()
async def callbacks(client, query):
    data = query.data.split("#")
    dirname = str(time.time())+"/"
    mkdir(dirname)
    message_id = data[0]
    chat_id = data[2]
    message = await app.get_messages(chat_id=chat_id, message_ids=int(message_id))
    await query.edit_text("Starting Your Download...")

    path = await message.download(dirname, progress=progressbar,
                                  progress_args=(query, time.time(), "Downloading"))
    await query.edit_text("Download Completed Starting Encoding...")
    newfname = "/".join(path.split("/")[:-1]) + "/" + "[" + data[1] + "] " + path.split("/")[-1]

    converter = Convert(data[1], path, newfname)
    converter.start()

    oldtxt = ""
    while True:
        newtxt = converter.progress
        if oldtxt != newtxt:
            await asyncio.sleep(5)
            if newtxt is not None:
                await query.edit_text(newtxt)
            oldtxt = newtxt
        if newtxt == "Completed Encoding":
            break
    if converter._done:
        await query.edit_text("Starting to Upload The file Now")
        await upload2tg(query, newfname)


@app.on_message(filters.command(["convert"]))
async def ffmpeg(client, message):
    try:
        if message.reply_to_message is None:
          try:
            await message.reply_text("🤬 Reply to telegram media 🤬")
          except:
            pass
          return
        File2Convert = message.reply_to_message
        chat_id = str(message.chat.id)
        message_id = str(message.message_id)
        keyboard = InlineKeyboard()
        keyboard.row(
            InlineKeyboardButton('240p', message_id + "#240#" + str(chat_id)),
            InlineKeyboardButton('360p', message_id + "#360#" + str(chat_id))
        )
        keyboard.row(
            InlineKeyboardButton('720p', message_id + "#720#" + str(chat_id)),
            InlineKeyboardButton('1080p', message_id + "#1080#" + str(chat_id))
        )
        keyboard.row(
            InlineKeyboardButton('480p', message_id + "#Compressed#" + str(chat_id))
        )
        await message.reply_text("Select The Option You Want", reply_markup=keyboard)
    except Exception as e:
        print("Error : "+str(e))
        await message.reply_text("Please Reply To A Valid Media File")


    
          
           
       
          
# run the application        
app.run()
