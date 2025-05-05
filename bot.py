from telegram.ext import Updater, CommandHandler
import os

TOKEN = os.environ.get('BOT_TOKEN')

def start(update, context):
    update.message.reply_text("🎬 VegaMoviesBot चालू है!")

# नया सिंटैक्स (use_context हटाएं)
updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler("start", start))
updater.start_polling()
updater.idle()
