# -*- coding: utf-8 -*-
import logging
from telegram.ext import Updater, MessageHandler, CommandHandler, Filters

import settings

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def start_bot(bot, update):
    hello_text = """Привет, милый {}! Я тут!
Как дела?
    """.format(update.message.chat.first_name)
    logging.info('{} /start'.format(update.message.chat.username))
    update.message.reply_text(hello_text)

def chat(bot, update):
    text = update.message.text
    logging.info(text)
    update.message.reply_text(text)

def main():
    upd = Updater(settings.API_KEY)
    
    upd.dispatcher.add_handler(CommandHandler('start', start_bot))
    upd.dispatcher.add_handler(MessageHandler(Filters.text, chat))

    upd.start_polling()
    upd.idle()

if __name__ == '__main__':
    logging.info('Bot started!')
    main()