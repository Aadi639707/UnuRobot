import os
from hydrogram import Client

# --- TELEGRAM API CONFIGURATION ---
API_ID = 27070308
API_HASH = "d1bfc4df9e7a49882cf91fc9f98fc8dd"
BOT_TOKEN = "8284596809:AAFutYvJvtxGBI0HjRm7uEO9cuTEufMRiCM"

# --- DATABASE CONFIGURATION ---
DB_URL = "mongodb+srv://aadi6397070:aadi6397@cluster55.fyd3s92.mongodb.net/?retryWrites=true&w=majority&appName=Cluster55"

# --- USER & PERMISSIONS ---
SUDO_USERS = [7876183821]
sudoers = SUDO_USERS

# --- GAME SETTINGS (Sabhi errors ka hal) ---
games = {}
player_game = {}
timeout = 60
minimum_players = 2 
maximum_players = 4 # Ye bhi add kar diya hai future error se bachne ke liye
sc = {}
msgs = {}

# --- INITIALIZING THE BOT CLIENT ---
bot = Client(
    "UnuRobot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="unu/plugins")
)
