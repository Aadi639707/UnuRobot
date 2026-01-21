import os
import asyncio
from hydrogram import idle
from config import bot
from unu.db import connect_database
from unu.utils import load_all, save_all

# --- DUMMY SERVER FOR RENDER PORT BINDING ---
from aiohttp import web

async def hello(request):
    return web.Response(text="Bot is Running!")

async def start_server():
    app = web.Application()
    app.router.add_get("/", hello)
    runner = web.AppRunner(app)
    await runner.setup()
    # Render automatically provides a PORT environment variable
    port = int(os.environ.get("PORT", 8080))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()
    print(f"Dummy server started on port {port}")

# --- MAIN BOT LOGIC ---
async def main():
    print("Connecting to Database...")
    await connect_database()
    
    print("Starting Dummy Server for Render...")
    await start_server()
    
    print("Starting Bot...")
    await bot.start()
    
    print("Loading Plugins...")
    await load_all()
    
    print("Bot is now Live!")
    
    try:
        await idle()
    except (KeyboardInterrupt, SystemExit):
        pass
    finally:
        print("Stopping Bot...")
        await save_all()
        await bot.stop()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    
