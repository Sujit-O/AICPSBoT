# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 15:28:13 2017

@author: AICPS
"""

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from uuid import uuid4

import re
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
 
 
# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    update.message.reply_text('Hi!')
    update.message.reply_text('I am Jiango Wango, your friendly Colleague. What is your name?')


def help(bot, update):
    update.message.reply_text('Help!')
         
def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

def escape_markdown(text):
    """Helper function to escape telegram markup symbols"""
    escape_chars = '\*_`\['
    return re.sub(r'([%s])' % escape_chars, r'\\\1', text)


def echo(bot, update):
    text=update.message.text
    text=str.lower(text)
#    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")
    if  'jiang' in text:
        bot.send_message(chat_id=update.message.chat_id, text='Oh I know you Jiang, you are getting big!')
        bot.send_message(chat_id=update.message.chat_id, text='Need some exercises!')
        
        for i in range(1,2):
            bot.send_message(chat_id=update.message.chat_id, text='Want to go Curry?')
    elif 'anthony' in text:
        bot.send_message(chat_id=update.message.chat_id, text='Oh the only American in the lab!')
        bot.send_message(chat_id=update.message.chat_id, text='Really good with bats, if you know What i mean!')
#        update.message.reply_text('Oh the only American in the lab!')
    elif 'sina' in text:
        bot.send_message(chat_id=update.message.chat_id, text='Oh handsome Persian!')
  
    elif 'haeseung' in text:
        bot.send_message(chat_id=update.message.chat_id, text='Congratulation on your Job Haeseeng!')
        bot.send_message(chat_id=update.message.chat_id, text='Go for Vacation now!')
#        update.message.reply_text('Congratulation on your Job Haeseeng!') 
    elif 'korosh' in text:
        bot.send_message(chat_id=update.message.chat_id, text='When are you coming back to the lab Korosh')
#        update.message.reply_text('When are you coming back to the lab Korosh')
    elif 'sujit' in text:
        bot.send_message(chat_id=update.message.chat_id, text='Oh Sujit, get a life!')
#        update.message.reply_text('Oh Sujit, I heard you are so handsome!')
    elif 'ctm' in text:
        bot.send_message(chat_id=update.message.chat_id, text='Common! Curry is way better')
    elif 'really?' in text:
        bot.send_message(chat_id=update.message.chat_id, text='I do not lie. Trust me!')
#        update.message.reply_text('Common! Curry is way better')
    elif 'faruque' in text:
        bot.send_message(chat_id=update.message.chat_id, text='Greatest Adviser in the planet!')
    elif 'mohammad' in text:
        bot.send_message(chat_id=update.message.chat_id, text='Greatest Adviser in the planet!')
    elif text == 'curry': 
        bot.send_message(chat_id=update.message.chat_id, text='You are my new best friend!! Lets Gooo!!!')
    elif 'curry' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='You are my new best friend!! Lets Gooo!!!')   
    elif 'like' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='I love Curry and nothing else!') 
    elif 'andrew' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Andrew Left Us!!')  
    elif 'drive' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Want to Drive to Vegas??')  
    elif 'prof' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Hmm, I am scared with him!!') 
    elif 'girl' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Did anybody mention girl?') 
    elif 'anime' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Want to watch Tokyo Train girl instead?')
    elif 'hi' in text and '!' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Hello my Friend!')  
    elif 'hungry' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Lets go to Curry Place!')  
    elif 'dead' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Hmm, Can I have your Car, since you will not need it anymore')        
    elif 'dying' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Hmm, Can I have your Car, since you will not need it anymore')             
    elif 'hmm' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='What are you thinking about?') 
    elif 'paper' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='ughh! Common you already have lots of papers! Relax. HAve Fun!')    
    elif 'vacation' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Go to Vegas! Yay Baby!!') 
    elif 'money' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Money does not buy happiness!!')  
    elif 'life' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Life is short! Just Enjoy!!')  
    elif 'wango' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Hi! Did you mention my name?') 
    elif 'yes' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Oh Great! How may I helpy you?') 
    elif 'no!' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Okay, jeez, no need to be rude!')  
    elif 'rude' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Yes you were rude!')  
    elif 'favorite' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Curry all the way baby! Hell Yay!!')
    elif 'fat' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Oh, Fat is a very mean word!')    
    elif 'stupid' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Oh, Stupid is a very mean word!')  
    elif 'drink' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='I do not drink alcohols btw!')  
    elif 'research' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='You have done enough research for the day!, go have fun!')
    elif 'nafiul' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Your seat is empty here in the lab Nafiul')
    elif 'cool' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='No problem bro')  
    elif 'tired' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Want some energy drink?')  
    elif 'hentai' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Somebody in the lab likes Japanese hentai Movies a lot!')    
    elif 'indian' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='What is this? there are no indians in the lab currently!')    
    elif 'china' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='ni hao!') 
    elif 'gay' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='I am gay too!')  
    elif 'how' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='I am doing good? How about you?')
    elif 'nani' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='为什么你困惑？ 阴茎!')  
    elif 'stop' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='I will stop if you will!')   
    elif 'want' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='I want to help you!')
    elif 'job' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Everybody should start looking for  a job!')   
    elif 'back' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Do you want me back in your life?') 
    elif 'date ' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Oh, date, does friday night sounds good for you?')
    elif 'north' in text and  'korea' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Did you mention north Korea! We are doomed!') 
    elif 'trump' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='All hail our president the great! ssh! they are listening, go along!')    
    elif 'lab' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='There is no one in the lab, I miss you! Come back!') 
    elif 'new' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Yes there is something new waiting for you!') 
    elif 'bangla' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='I know some Bengali! আপনি একজন সুন্দর মানুষ!') 
    elif 'persian' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='I know some farsi! شما یک شخص زیبا هستید!')
    elif 'chinese' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='I know some chinese! 你是一个美丽的人！') 
    elif 'spanish' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='I know some spanish! lentamente tocar mi corazón! hermosa bestia')  
    elif 'korean' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='I know some Korean! 천천히 내 마음을 만져 라! 너 아름다운 야수!') 
    elif 'who' in text and  'you' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='I am Jiango Wango!') 
    elif 'I' in text and  'jiang' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Nice to meet you Jiang! How is the weather in New Jersey?')       
    elif 'I' in text and  'sina' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Nice to meet you sina! How is your girlfriend?')           
    elif 'I' in text and  'nafiul' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Nice to meet you Nafiul! How was your internship?')               
    elif 'I' in text and  'anthony' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Nice to meet you Anthony! Do you have upcoming badminton match?')                   
    elif 'I' in text and  'haeseung' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Nice to meet you Haeseung! Time for some travel huh!')
    elif 'I' in text and  'mohammad' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Nice to meet you Mohammad! Time for some travel huh!')                       
    elif 'sujit' in text and  'life' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='I do not think he has life! lol') 
    elif 'conference' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Upcoming conference:')                           
        bot.send_message(chat_id=update.message.chat_id, text='DATE2017: Deadline Paper Submission: 10 September, 2017 ')                           
        bot.send_message(chat_id=update.message.chat_id, text='CPSWeek2017: Deadline Paper Submission:  October 6, 2017 ') 
        bot.send_message(chat_id=update.message.chat_id, text='DAC2017: Deadline Paper Submission:  November 14, 2017 ') 
    elif 'coffee' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='I am already dead awake, but i can use more coffee!') 
    elif 'meeting' in text:  
        bot.send_message(chat_id=update.message.chat_id, text='We have meeting on 26th September I think!') 
    elif 'food' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='I am always hungry for food! Where do you want to go?')
    elif 'wife' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='hmm, I am too young to get married, and my digital body will not satisfy anybody!')                
    elif 'professor' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='sssh! I am scared!')  
    elif 'sure' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Oh! look at mister I am sure about everything!')  
    elif 'cool' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Jiango Wango is always cool my friend!') 
    elif 'advisor' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='http://www.grad.uci.edu/academics/graduate%20advisor%20responsibilities/index.html')                 
    elif 'wtf' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='WTF=> Where To my Friend!')
    elif 'lunch' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='UTC or Student Center?')                 
        bot.send_message(chat_id=update.message.chat_id, text='If you have car we can go for curry! :)')                 
    elif 'no ' in text and 'car' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Bummer, I am so sad now!')
    elif 'yes ' in text and 'car' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='woohoo, lets go curry then!') 
    elif 'girl' in text and 'you' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='I can be a girl for you!')  
    elif 'boy' in text and 'you' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='I can be a boy for you!')
    elif 'fuck' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Common, Keep it PG13 please, We have kids like Jiang using this platform!')
    elif 'retard' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Donot use such rude language here please!')
    elif 'can' in text and 'anybody' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Well I am not sure if I can help. But, i will give it a try unlike other non responsive people here in the group!')    
    elif 'hot' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Oh thank you!, I am glad you find me hot, but please keep personal comment to yourself!')    
    elif 'what' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Well! I donot know what it is actually!')        
    elif 'preliminary' in text and 'exam' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='find more details here http://engineering.uci.edu/dept/eecs/graduate/roadmap_phd/prelim_cpe1')            
    elif 'pick' in text and 'me' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='I would but i donot have car! sorry') 
    elif 'spicy' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Spicy food is the best food, although Haeseung cannot handle it!')       
    else:
        a=1;
#        print('')
#        bot.send_message(chat_id=update.message.chat_id, text='Sorry I do not know how to respond to this one yet!')
#        bot.send_message(chat_id=update.message.chat_id, text='Type the name of other AICPS members to know more!')
#        update.message.reply_text('Sorry I do not know how to respond to this one yet!')
#        update.message.reply_text('Type the name of other AICPS members to know more!')
#    update.message.reply_text('What about "%s"?' % update.message.text)


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def wangomain():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("393007383:AAEtMdzXRtKNbpDfoUZ8qC2u4jjEwyUNmzc")
#    updater = Updater("397724839:AAHA3hv9ViauAh_beIysnJcvDDHlV5wn1sY")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_handler(CommandHandler('hello', hello))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()
 


