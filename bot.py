from telegram.ext import Updater, CommandHandler
import os

TOKEN = os.environ.get('BOT_TOKEN')

def start(update, context):
    update.message.reply_text("🎬 VegaMoviesBot चालू है!")

updater = Updater(TOKEN, use_context=True)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.start_polling()
updater.idle()
