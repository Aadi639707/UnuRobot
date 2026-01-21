import os

# --- TELEGRAM API CONFIGURATION ---
# These are your personal API details from my.telegram.org
API_ID = 27070308
API_HASH = "d1bfc4df9e7a49882cf91fc9f98fc8dd"

# This is your Bot Token from @BotFather
BOT_TOKEN = "8284596809:AAFutYvJvtxGBI0HjRm7uEO9cuTEufMRiCM"

# --- DATABASE CONFIGURATION ---
# Your MongoDB connection string
DB_URL = "mongodb+srv://sanatanigojo4_db_user:Aadi639707@clonecartbot.a8bu3xa.mongodb.net/?retryWrites=true&w=majority&appName=ClonecartBot"

# --- USER & PERMISSIONS ---
# List of user IDs allowed to use sudo/admin commands
SUDO_USERS = [7876183821]
sudoers = SUDO_USERS

# --- BOT INTERNALS (REQUIRED BY UNUROBOT) ---
# These variables fix the "ImportError: cannot import name 'games'"
games = {}
player_game = {}

# Placeholder for the bot instance
bot = None
