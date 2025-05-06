from telegram.ext import ApplicationBuilder, CommandHandler
from fastapi import FastAPI
import uvicorn
import os
from threading import Thread

# Create FastAPI app for health checks
app = FastAPI()

@app.get("/")
def health_check():
    """Endpoint for health checks"""
    return {"status": "VegaMoviesBot is running"}

async def start(update, context):
    """Handler for /start command"""
    await update.message.reply_text("🎬 VegaMoviesBot is running!")

def run_bot():
    """Function to run the Telegram bot"""
    TOKEN = os.environ['BOT_TOKEN']
    
    # Initialize and configure bot
    bot = ApplicationBuilder().token(TOKEN).build()
    bot.add_handler(CommandHandler("start", start))
    
    # Start polling for updates
    bot.run_polling()

if __name__ == "__main__":
    # Start bot in a separate daemon thread
    bot_thread = Thread(target=run_bot, daemon=True)
    bot_thread.start()
    
    # Run FastAPI server on main thread for health checks
    uvicorn.run(app, host="0.0.0.0", port=8000)
