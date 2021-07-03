import Constants as keys
from telegram.ext import *

print("Botted")

#corresponds to the /start command in TG
def start_command(update, context):
    update.message.reply_text("Let's gooooooo!")

#corresponds to the /help command in TG
def help_command(update, context):
    update.message.reply_text('Type the NRIC you wanna check without the last letter')

#corresponds to any other text in TG    
def handle_message(update, context):
    text = str(update.message.text).upper()
    response = responses(text)
    update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} caused error {context.error}")

#logic reasoning whether to pass the checking function
def responses(input_text):
    user_message = str(input_text).upper()

    if user_message[0] in "STFG" and len(user_message)==8:
        return (generate_last_letter(user_message))
    else : 
        return ("Try again, mortal")

#actual checking function
def generate_last_letter(nric):
    prefix = nric[0]
    # suffix = nric[-1].upper()
    number_string = nric[1:]
    numbers = []

    fg_map = ['X', 'W', 'U', 'T', 'R', 'Q', 'P', 'N', 'M', 'L', 'K']
    st_map = ['J', 'Z', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']

    for n in number_string:
        numbers.append(int(n))
    weights = [2, 7, 6, 5, 4, 3, 2]

    number_sum = 0
    for w, n in zip(weights, numbers):
        number_sum += n * w
    
    if prefix == 'T' or prefix == 'G':
        number_sum += 4

    remainder = number_sum % 11

    if prefix == 'F' or prefix == 'G':
        return fg_map[remainder]

    if prefix == 'S' or prefix == 'T':
        return st_map[remainder]

#adds handlers for integration with Telegram
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