import telebot
import urllib.request
import os
import praw 
import threading

bot_token = '835075644:AAERQCEPXSjpc-Z9SvZFPFcbPXNfiLUS3QI'
bot = telebot.TeleBot(token=bot_token)
reddit = praw.Reddit(client_id= 'D1O4NdmXoZVNpg', client_secret= 'voQJq4BVb4DWL8WMFCsmiZRzou4', username= 'tgdankbot', password= 'Kutaluta@3crest', user_agent= 'v1' )
subreddit = reddit.subreddit('dankmemes')
hot_memes = subreddit.top('day',limit=20)
url_arr = [None]*20



def update_urls():
    i = 0
    for submission in hot_memes:
        if not submission.stickied:
            url_arr[i] = (submission.url)
            i += 1


def dl(url):
    f = open('pic.jpg', 'wb')
    f.write(urllib.request.urlopen(url).read())
    f.close

def send_photo(): 
    threading.Timer(88400,send_photo).start()
    update_urls()
    for i in range(0,20):
        dl(url_arr[i])
        img = open('pic.jpg','rb')
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

