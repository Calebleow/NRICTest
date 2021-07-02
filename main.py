import Constants as keys
from telegram.ext import *
import json 
import requests
import time
import urllib

print("Botted")

TOKEN = keys
URL = "https://api.telegram.org/bot{}/".format(TOKEN.API_KEY)


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates(offset=None):
    url = URL + "getUpdates?timeout=100"
    if offset:
        url += "&offset={}".format(offset)
    js = get_json_from_url(url)
    return js

def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)

def echo_all(updates):
    for update in updates["result"]:
        try:
            text = update["message"]["text"]
            chat = update["message"]["chat"]["id"]
            send_message(text, chat)
        except Exception as e:
            print(e)

def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)


def send_message(text, chat_id):
    text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)
    
text, chat = get_last_chat_id_and_text(get_updates())
send_message(text, chat)

def main():
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            echo_all(updates)
        time.sleep(0.5)

#Logical reasoning here
def responses(input_text):
    user_message = str(input_text)

    if user_message in ("S","T","F","G"):
        return (generate_last_letter(nric))
    else : 
        return ("Try again mortal")

def generate_last_letter(nric):
    prefix = nric[0].upper()
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

nric = text

if __name__ == '__main__':
    main()