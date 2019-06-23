import telebot
import urllib.request
import os
import praw 
import threading

bot_token = '828581923:AAEUVgE8KBPhEqkEjePEuS0RiRmoYDg2W_Q'
bot = telebot.TeleBot(token=bot_token)
reddit = praw.Reddit(client_id= 'CYJNh3ecbQhxzQ', client_secret= 'du58jAIgpE9lbfXoLoJlkEUnl4Y', username= 'tgdankbot', password= 'Kutaluta@3crest', user_agent= 't5' )
subreddit = reddit.subreddit('aww')
hot_aww = subreddit.top('day',limit=20)
url_arr = []

def update_urls():
    url_arr.clear()
    for i in range(0,20):
        for submission in hot_aww:
            if 'jpg' in submission.url:
                url_arr.append(submission.url)
                print(url_arr[i])


def dl(url):
    f = open('pic.jpg', 'wb')
    if 'jpg' in url:
        f.write(urllib.request.urlopen(url).read())
    f.close


def send_photo(): 
    threading.Timer(88400,send_photo).start()
    update_urls()
    count = len(url_arr)
    for i in range(0,count):
        if(url_arr[i] is not None):
            dl(url_arr[i])
            img = open('pic.jpg','rb')
            if os.stat('pic.jpg').st_size != 0:
                bot.send_photo(chat_id ='@testingbottg',photo = img)
            img.close


@bot.message_handler(commands = ['start'])
def send_welcome(message):
    bot.reply_to(message, 'Welcome, press /help for more information')

@bot.message_handler(commands = ['help'])
def send_welcome(message):
    bot.reply_to(message, 'Hit /send')

@bot.message_handler(func=lambda message: 'send 384252204' in message.text)
def every24(message):
        send_photo()
        
def listener(messages):
    for m in messages:
        print(str(m))


bot.set_update_listener(listener)
bot.polling()

