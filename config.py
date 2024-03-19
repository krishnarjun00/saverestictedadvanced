from os import environ 

class Config:
    API_ID = 26765615
    API_HASH = "dc9335059a80b3c8753d26e36d9e28f4"
    BOT_TOKEN = "6992559223:AAEMce2gy8ALQPi7pLe8I6PLfjbuOTWBlHc"
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = "mongodb+srv://mswpresents01:O1mAmjU4SHgEergF@cluster0.swcwpvm.mongodb.net/?retryWrites=true&w=majority"
    DATABASE_NAME = environ.get("DATABASE_NAME", "hacker")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6389088397').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
