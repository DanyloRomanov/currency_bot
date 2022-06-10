from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
from scrape_rates import get_rate_for_currency

PORT = int(os.environ.get('PORT', '8443'))
main_message = '''
Please select the currency and see the most up to date rates
USD click or type /usd
EURO click or type /euro
GBP click or type /gbp'''


# function to handle the /start command
def start(update, context):
    first_name = update.message.chat.first_name
    update.message.reply_text(f'Hi {first_name}!\n {main_message}')


def get_usd(update, context):
    update.message.reply_text(get_rate_for_currency('usd'))
    update.message.reply_text(main_message)


def get_gbp(update, context):
    update.message.reply_text(get_rate_for_currency('gbp'))
    update.message.reply_text(main_message)


def get_euro(update, context):
    update.message.reply_text(get_rate_for_currency('euro'))
    update.message.reply_text(main_message)


def help(update, context):
    first_name = update.message.chat.first_name
    update.message.reply_text(f'Hey {first_name}!\n This bot can help you to get most current currency exchange rates')
    update.message.reply_text(main_message)


# function to handle normal text
def text(update, context):
    text_received = update.message.text
    update.message.reply_text(f'You said "{text_received}",I am programmed to take only couple commands')
    update.message.reply_text(main_message)


def main():
    TOKEN = "5438627941:AAF2qdXdkhzZTrn0yb-pSOvKgTiJRiOHsos"

    # create the updater, that will automatically create also a dispatcher and a queue to
    # make them dialogue
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # add handlers for start and help commands
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(CommandHandler("usd", get_usd))
    dispatcher.add_handler(CommandHandler("euro", get_euro))
    dispatcher.add_handler(CommandHandler("gbp", get_gbp))

    # add handler for normal text (not commands)
    dispatcher.add_handler(MessageHandler(Filters.text, text))

    # start your shiny new bot
    # updater.start_polling()
    updater.start_webhook(listen='0.0.0.0',
                          port=int(PORT),
                          url_path=TOKEN,
                          webhook_url=f'https://shielded-hamlet-79363.herokuapp.com/{TOKEN}')

    # run the bot until Ctrl-C
    updater.idle()


if __name__ == '__main__':
    main()
