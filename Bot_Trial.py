from telegram.ext import Updater, MessageHandler, Filters
import urllib
import wget
import ingredientRecommendation
import cuisineRecommendation
import numpy as np


#To Make List of Numbers into an int
def list_to_int(list):
    a=''
    for i in List:
        a+=str(i)
    a=int(a)
    return(a)

updater = Updater(token='819485419:AAGaFJ5QfpGjLKeCkRETgL7BmUQA2bTfOa0')
dispatcher = updater.dispatcher

#For Exception Handling
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Hey!Send in a picture of what you're buying and we'll suggest what can go with it!")

#Start Bot
from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

#Meme is made and sent
def echo(bot, update):
    file = bot.getFile(update.message.photo[-1].file_id)
    file_url = (file.file_path)
    file_name = wget.download(file_url)
    x=[]

    x=ingredientRecommendation.Ingredient_reco(file_name)
    y=cuisineRecommendation.cuisine_recommend(file_name)

    print(type(y))
    ts = y.tolist()
    cuisine=""
    cuisine="Predicted Cuisine: "+ts[0]
    bot.send_message(chat_id=update.message.chat_id, text=cuisine)
    cuisine="Here's a few "+ts[0]+" ingredients that could go with that:"
    bot.send_message(chat_id=update.message.chat_id, text=cuisine)
    for i in x:
        bot.send_message(chat_id=update.message.chat_id, text=i)


echo_handler = MessageHandler(Filters.photo, echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()
