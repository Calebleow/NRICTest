import Constants as keys
from telegram.ext import *
import Responses as R

print("Botted")

def start_command(update, context):
    update.message.reply_text('lets go')

def help_command(update, context):
    update.message.reply_text('Type the NRIC you wanna check without the last letter')
    
def handle_message(update, context):
    text = str(update.message.text).upper()
    response = R.responses(text)

    update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()