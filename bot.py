from telegram.ext import ApplicationBuilder, CommandHandler
import os
import logging

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Get token from environment variables
TOKEN = os.environ.get('BOT_TOKEN')

async def start(update, context):
    """Handler for the /start command"""
    await update.message.reply_text(
        "🎬 **VegaMoviesBot is running!**\n\n"
        "Available commands:\n"
        "/start - Start the bot\n"
        "/movies - Browse all movies"
    )

async def movies(update, context):
    """Handler for the /movies command"""
    await update.message.reply_text("🍿 All movies: https://vegamoviess.fun")

def main():
    """Start the bot"""
    # Create the Application
    app = ApplicationBuilder().token(TOKEN).build()
    
    # Add command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("movies", movies))
    
    # Start the bot
    print("Bot is starting...")
    app.run_polling()

if __name__ == '__main__':
    main()
