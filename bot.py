from telegram.ext import ApplicationBuilder, CommandHandler
from fastapi import FastAPI
import uvicorn
import os
import asyncio
import threading

app = FastAPI()

@app.get("/")
def health_check():
    return {"status": "VegaMoviesBot चालू है"}

async def start(update, context):
    await update.message.reply_text("🎬 VegaMoviesBot चालू है!")

async def run_bot():
    """बॉट को async तरीके से चलाता है"""
    TOKEN = os.environ['BOT_TOKEN']
    bot = ApplicationBuilder().token(TOKEN).build()
    bot.add_handler(CommandHandler("start", start))
    await bot.run_polling()

def start_bot():
    """थ्रेड के अंदर नया इवेंट लूप बनाता है"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(run_bot())

if __name__ == "__main__":
    # बॉट को अलग थ्रेड में चलाएं
    bot_thread = threading.Thread(target=start_bot, daemon=True)
    bot_thread.start()
    
    # मुख्य थ्रेड में FastAPI सर्वर चलाएं
    uvicorn.run(app, host="0.0.0.0", port=8000)
