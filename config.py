import os
from hydrogram import Client

# --- TELEGRAM API CONFIGURATION ---
API_ID = 27070308
API_HASH = "d1bfc4df9e7a49882cf91fc9f98fc8dd"
BOT_TOKEN = "8284596809:AAFutYvJvtxGBI0HjRm7uEO9cuTEufMRiCM"

# --- DATABASE CONFIGURATION ---
DB_URL = "mongodb+srv://sanatanigojo4_db_user:Aadi639707@clonecartbot.a8bu3xa.mongodb.net/?retryWrites=true&w=majority&appName=ClonecartBot"

# --- USER & PERMISSIONS ---
SUDO_USERS = [7876183821]
sudoers = SUDO_USERS

# --- BOT INTERNALS ---
games = {}
player_game = {}
timeout = 60
sc = {}
msgs = {}

# --- INITIALIZING THE BOT CLIENT ---
# This line fixes the 'NoneType' object has no attribute 'start' error
bot = Client(
    "UnuRobot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)
