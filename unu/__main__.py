import os
import asyncio
from hydrogram import idle
from aiohttp import web
from config import bot
from unu.db import connect_database
from unu.utils import load_all, save_all

# --- DUMMY SERVER FOR RENDER ---
async def hello(request):
    return web.Response(text="Bot is Alive and Running!")

async def start_server():
    app = web.Application()
    app.router.add_get("/", hello)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.environ.get("PORT", 8080))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()
    print(f"Web server started on port {port}")

# --- MAIN ENGINE ---
async def main():
    print("Connecting to Database...")
    await connect_database()
    
    print("Starting Dummy Server...")
    await start_server()
    
    print("Logging into Telegram...")
    me = await bot.start()
    print(f"Logged in as: @{me.username}")
    
    print("Loading Plugins...")
    await load_all()
    
    print("--- BOT IS NOW LIVE ---")
    
    try:
        await idle()
    except (KeyboardInterrupt, SystemExit):
        pass
    finally:
        print("Saving data and shutting down...")
        await save_all()
        await bot.stop()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    
