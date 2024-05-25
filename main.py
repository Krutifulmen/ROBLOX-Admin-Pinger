from telegram.ext import Updater, CommandHandler
import requests
import time

site = "https://www.roblox.com/users/1193694687/"
 
def start(update, context):
    update.message.reply_text( "📍 Hello, I will ping you when the ROBLOX Admins are Online! \n Work only on events, and only on one admin - InceptionTime ✅ \n , Errors? - contact me: @murkote_kot 💬 \n Spamming/Flooding = Block 😉 \n Good using it! ❤️‍")
    
def send_message(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"🟢 InceptionTime is Online! Here is a link for you: {site}. Join him! 🤗")

updater = Updater('YOUR TELEGRAM BOT TOKEN', use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler('start', start))
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, send_message))


while True:
    result = requests.get(site)
    result = result.text
    if "Online" in result:
        send_message()
    else:
	    pass

updater.start_polling()
