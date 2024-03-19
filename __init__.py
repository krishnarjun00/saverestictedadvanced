#Join me at telegram @dev_gagan

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)


# variables
API_ID = 26765615
API_HASH = "dc9335059a80b3c8753d26e36d9e28f4"
BOT_TOKEN = "7012933656:AAG5uHDGRQHwH4WhUPi1LKSmQXHt_JDnsFQ"
SESSION = "BQGYaS8ASNnD0e3uXTGHnO-dhEbCVIxOiDLhQjtg1CB_PD9nw3RSa2nL1P2wlPAsRqc8mKd8pgEDsz1ubVCaPQ_STaNvOQWAAdmx2uUx-FAimoCTDwgvIpWqS9aKoF2tH-ZCEVNbAkbvgEQBMV9ZPtQ0bYdPJ5LRvzSyOUlVGOX1ao_D6Cw_tl2LrxU9WatUlEv6TB1JFEcVIi6RrAe_IpjmF5RMSJdH8TPkM7K7Umxw6Pwx4xKD2I6R3jQRDfWAQ2YDnfKndC1xJkZo5DWb4D7iF-jX9Eqz_fuD3L2gudKPC_IbcgKsYgjLknAJxJzicjV_0DWGa_E6RdEKQbAz72XwACETzAAAAAF80cCNAA"
FORCESUB = "hackermittron"
AUTH = 6389088397
SUDO_USERS = []


bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("myacc",api_id=API_ID,api_hash=API_HASH,session_string=SESSION)

try:
    userbot.start()
except BaseException:
    print("Your session expired please re add that... thanks ɧąƈƙɛཞ. 🔛🔝.")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    #print(e)
    logger.info(e)
    sys.exit(1)
