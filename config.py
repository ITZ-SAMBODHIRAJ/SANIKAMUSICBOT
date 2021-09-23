import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "𝙉𝙖𝙪𝙜𝙝𝙩𝙮 ✘ 𝙎𝙩𝙪𝙙𝙚𝙣𝙩")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/10e55ad845c9a798d6c63.jpg")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/10e55ad845c9a798d6c63.jpg")
BOT_IMG = getenv("BOT_IMG", "https://telegra.ph/file/dd84c12e527a609d7eebf.jpg")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/e026dd4ccda9d334975e0.jpg")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/e026dd4ccda9d334975e0.jpg")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME", "Noughty_Student_Bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "𝙉𝙖𝙪𝙜𝙝𝙩𝙮 ✘ 𝙎𝙩𝙪𝙙𝙚𝙣𝙩")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "naughty_stud_ents")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "naughty_stud_ents")
OWNER_NAME = getenv("OWNER_NAME", "Timesisnotwaiting") # isi dengan username kamu tanpa simbol @
PMPERMIT = getenv("PMPERMIT", None)
OWNER_ID = int(os.environ.get("OWNER_ID")) # fill with your id as the owner of the bot
DATABASE_URL = os.environ.get("DATABASE_URL") # fill with your mongodb url
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL")) # make a private channel and get the channel id
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False)) # just fill with True or False (optional)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
