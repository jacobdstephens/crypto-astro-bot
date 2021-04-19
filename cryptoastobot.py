#!/usr/bin/env python3
import Constants as keys
import Responses as R
import requests
import json

from telegram import *
from telegram.ext import *

print("Bot Started....")


def start_command(update, context):
    update.message.reply_text("Would you like me to give you an astrology reading?")

def help_command(update, context):
    update.message.reply_text("God helps those that help themselves.")

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.responses(text)

    if 'birthdata' not in context.user_data:
        print('No Data')

    update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
    updater=Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    # Slash command handlers
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    
    # Add message handler
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
