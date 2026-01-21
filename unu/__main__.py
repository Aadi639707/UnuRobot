import os
import asyncio
from hydrogram import idle
from tortoise import run_async

from config import bot
from unu.db import connect_database
from unu.utils import load_all, save_all
from unu.version import ascii_art

async def main():
    # Clear screen and show bot branding
    if os.name == 'posix':
        os.system("clear")
    print(ascii_art)
    
    print("Connecting to Database...")
    await connect_database()
    
    print("Starting Bot...")
    await bot.start()
    
    print("Loading Plugins...")
    await load_all()
    
    print("Bot is now Live!")
    
    # Using a try-except block to handle Render's signal issues
    try:
        await idle()
    except (KeyboardInterrupt, SystemExit):
        pass
    finally:
        print("Stopping Bot...")
        await save_all()
        await bot.stop()

if __name__ == "__main__":
    # Standard way to run async main in Python
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    
