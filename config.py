import os

# --- TELEGRAM API CONFIGURATION ---
API_ID = 27070308
API_HASH = "d1bfc4df9e7a49882cf91fc9f98fc8dd"
BOT_TOKEN = "8284596809:AAFutYvJvtxGBI0HjRm7uEO9cuTEufMRiCM"

# --- DATABASE CONFIGURATION ---
DB_URL = "mongodb+srv://sanatanigojo4_db_user:Aadi639707@clonecartbot.a8bu3xa.mongodb.net/?retryWrites=true&w=majority&appName=ClonecartBot"

# --- USER & PERMISSIONS ---
SUDO_USERS = [7876183821]
sudoers = SUDO_USERS

# --- BOT INTERNALS (Fixes the current errors) ---
games = {}
player_game = {}
timeout = 60 # This fixes the 'timeout' ImportError
# Adding these just in case they are needed next:
sc = {}
msgs = {}

# Hydrogram Instance
bot = None
