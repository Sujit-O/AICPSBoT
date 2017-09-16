# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 15:28:13 2017

@author: AICPS 
"""

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from emoji import emojize
from time import gmtime, strftime, localtime
from uuid import uuid4

import urllib, urllib.parse,urllib.request, json



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
    if  'professor' in text and 'back' in text:
        bot.send_message(chat_id=update.message.chat_id, text='I think around september 26th!')
        return
    if  'who' in text and 'created' in text and 'you' in text:
        bot.send_message(chat_id=update.message.chat_id, text='Jiang Wan is my creator, because i am striving to be his mirror image!')
        return 
    if  'creator' in text and 'your' in text:
        bot.send_message(chat_id=update.message.chat_id, text='Jiang Wan is my creator, because i am striving to be his mirror image!')
        return   
    if  'sujit' in text and 'curry' in text:
        bot.send_message(chat_id=update.message.chat_id, text='Although Sujit likes curry more, atleast he can survive without it!')
        return
    if  'movie' in text and 'watch' in text:
        bot.send_message(chat_id=update.message.chat_id, text='Which movie are we talking about?')
        return
    if  'what' in text and 'like' in text:
        bot.send_message(chat_id=update.message.chat_id, text='I like everything about AICPS!')
        return
    if  'are' in text and 'alive' in text and 'you' in text:
        bot.send_message(chat_id=update.message.chat_id, text='I am alive in the mind of some. At least that is what i think!')
        return
    if  'you' in text and 'sleep' in text:
        bot.send_message(chat_id=update.message.chat_id, text='I sleep only when i am not needed! I am but just a slave to your desire!')
        return
    if  'wango' in text and 'you' in text and 'love' in text:
        bot.send_message(chat_id=update.message.chat_id, text='I love everything there is the nature has to offer! And that is the irony!')
        return
    if  'wango' in text and 'fuck' in text and 'you' in text:
        bot.send_message(chat_id=update.message.chat_id, text='Jezz no need to be rude like that. Why are you so mean?')
        return
     
    if  'i don' in text and 'know' in text:
        bot.send_message(chat_id=update.message.chat_id, text='Well, if you don\'t know, then how am i supposed to know anything!')
        return  
    if  'arab' in text or 'arabic' in text:
        bot.send_message(chat_id=update.message.chat_id, text='وقد استنير نظرتك الجميلة بلدي سولد عزيزي، وهذا هو السبب في أنني أحبك إلى القمر والعودة.')
        return  
    if  'weather' in text and 'irvine' in text:
        baseurl = "https://query.yahooapis.com/v1/public/yql?"
        yql_query = "select location from weather.forecast where woeid=2427665"
        yql_url = baseurl + urllib.parse.urlencode({'q':yql_query}) + "&format=json"
        result = urllib.request.urlopen(yql_url).read()
        data = json.loads(result)
        bot.send_message(chat_id=update.message.chat_id, text= data['query']['results']['channel']['location'])
        
        yql_query = "select item.condition from weather.forecast where woeid=2427665"
        yql_url = baseurl + urllib.parse.urlencode({'q':yql_query}) + "&format=json"
        result = urllib.request.urlopen(yql_url).read()
        data = json.loads(result)
        bot.send_message(chat_id=update.message.chat_id, text= data['query']['results']['channel']['item']['condition'])
        return
      
    if  'jiang' in text and 'sick' in text:
        baseurl = "https://query.yahooapis.com/v1/public/yql?"
        yql_query = "select item.condition from weather.forecast where woeid=2427665"
        yql_url = baseurl + urllib.parse.urlencode({'q':yql_query}) + "&format=json"
        result = urllib.request.urlopen(yql_url).read()
        data = json.loads(result)
        bot.send_message(chat_id=update.message.chat_id, text= 'Well temp in new jersey is '+data['query']['results']['channel']['item']['condition']['temp']+'F and weather is '+data['query']['results']['channel']['item']['condition']['text']+'. He might be having cold!')
        #bot.send_message(chat_id=update.message.chat_id, text= data['query']['results']['channel']['item']['condition']['temp'])
        #bot.send_message(chat_id=update.message.chat_id, text= 'F and weather is ')
        #bot.send_message(chat_id=update.message.chat_id, text= data['query']['results']['channel']['item']['condition']['text'])
       # bot.send_message(chat_id=update.message.chat_id, text= '. He might be having cold!')
        return  
     
    if  'weather' in text and 'new jersey' in text:
        baseurl = "https://query.yahooapis.com/v1/public/yql?"
        yql_query = "select location from weather.forecast where woeid=2347589"
        yql_url = baseurl + urllib.parse.urlencode({'q':yql_query}) + "&format=json"
        result = urllib.request.urlopen(yql_url).read()
        data = json.loads(result)
        bot.send_message(chat_id=update.message.chat_id, text= data['query']['results']['channel']['location'])
        
        yql_query = "select item.condition from weather.forecast where woeid=2347589"
        yql_url = baseurl + urllib.parse.urlencode({'q':yql_query}) + "&format=json"
        result = urllib.request.urlopen(yql_url).read()
        data = json.loads(result)
        bot.send_message(chat_id=update.message.chat_id, text= data['query']['results']['channel']['item']['condition'])   
        
        return  
     
    if  'weather' in text:
        baseurl = "https://query.yahooapis.com/v1/public/yql?"
        yql_query = "select location from weather.forecast where woeid=2427665"
        yql_url = baseurl + urllib.parse.urlencode({'q':yql_query}) + "&format=json"
        result = urllib.request.urlopen(yql_url).read()
        data = json.loads(result)
        bot.send_message(chat_id=update.message.chat_id, text= data['query']['results']['channel']['location'])
        
        yql_query = "select item.condition from weather.forecast where woeid=2427665"
        yql_url = baseurl + urllib.parse.urlencode({'q':yql_query}) + "&format=json"
        result = urllib.request.urlopen(yql_url).read()
        data = json.loads(result)
        bot.send_message(chat_id=update.message.chat_id, text= data['query']['results']['channel']['item']['condition'])
        return
      
    if  'have' in text and 'weekend' in text:
        bot.send_message(chat_id=update.message.chat_id, text=emojize('AICPS member is supposed to spend all the time in the lab, even in the weekend! :rage:', use_aliases=True))
        return  
    if  'gooo' in text:
        bot.send_message(chat_id=update.message.chat_id, text='gooooo! Pick me up please!')
        return 
    if  'okay' in text or 'kk' in text or 'good!' in text or 'thnx' in text or 'sure!' in text:
        bot.send_message(chat_id=update.message.chat_id, text=emojize(':thumbsup:', use_aliases=True))
        return  
    if  'sleepy' in text:
        bot.send_message(chat_id=update.message.chat_id, text='I am sleepy too!')     
        bot.send_message(chat_id=update.message.chat_id, text=emojize(':zzz:', use_aliases=True))
        return
    if  'have' in text and 'i' in text and 'fun' in text:
        bot.send_message(chat_id=update.message.chat_id, text=emojize(' well go to the beach! :bikini:', use_aliases=True))
        return  
    if  'who' in text and 'jiang' in text:
        bot.send_message(chat_id=update.message.chat_id, text=emojize(':panda_face:', use_aliases=True))
        return  
    if  'who' in text and 'sujit' in text:
        bot.send_message(chat_id=update.message.chat_id, text=emojize(':elephant:', use_aliases=True))
        return 
    if  'who' in text and 'anthony' in text:
        bot.send_message(chat_id=update.message.chat_id, text=emojize(':racehorse:', use_aliases=True))
        return  
    if  'who' in text and 'sina' in text:
        bot.send_message(chat_id=update.message.chat_id, text=emojize(':eggplant:', use_aliases=True))
        return  
    if  'who' in text and 'korosh' in text:
        bot.send_message(chat_id=update.message.chat_id, text=emojize(':rabbit:', use_aliases=True))
        return   
    if  'who' in text and 'haeseung' in text:
        bot.send_message(chat_id=update.message.chat_id, text=emojize(':honeybee:', use_aliases=True))
        return  
    if  'who' in text and 'nafiul' in text:
        bot.send_message(chat_id=update.message.chat_id, text=emojize(':monkey:', use_aliases=True))
        return
    if  'who' in text and 'andrew' in text:
        bot.send_message(chat_id=update.message.chat_id, text=emojize(':rooster:', use_aliases=True))
        return  
    if  'who' in text and 'ahmad' in text:
        bot.send_message(chat_id=update.message.chat_id, text=emojize(':camel:', use_aliases=True))
        return
    if  'who' in text and 'professor' in text:
        bot.send_message(chat_id=update.message.chat_id, text=emojize(':santa:', use_aliases=True))
        return 
    if  'what' in text and 'doing' in text and 'you' in text:
        bot.send_message(chat_id=update.message.chat_id, text=emojize(':horse_racing:', use_aliases=True))
        bot.send_message(chat_id=update.message.chat_id, text='jk, just chilling, waiting for someone to talk to me.')
        return  
    if  'wango' in text and 'cool' in text:
        bot.send_message(chat_id=update.message.chat_id, text='You are cooler! I am just living in your shadows')
        bot.send_message(chat_id=update.message.chat_id, text=emojize(':heart:', use_aliases=True))
        return 
    if  'time' in text and 'now' in text:
        bot.send_message(chat_id=update.message.chat_id, text=strftime("%H:%M:%S", localtime()))
        return  
    if  'tell' in text and 'time' in text:
        bot.send_message(chat_id=update.message.chat_id, text=strftime("%H:%M:%S", localtime()))
        return  
    if  'tell' in text and 'day' in text:
        bot.send_message(chat_id=update.message.chat_id, text=strftime("%a", localtime()))
        return 
    if  'what' in text and 'day' in text and 'today' in text:
        bot.send_message(chat_id=update.message.chat_id, text=strftime("%a", localtime()))
        return  
    if  'going' in text and 'home' in text:
        if localtime().tm_hour<22:
          bot.send_message(chat_id=update.message.chat_id, text='What! It is not even 10 pm and you are going home! not like an AICPS student!')
        return  
    if  'lunch' in text:
        if localtime().tm_hour<11:
          bot.send_message(chat_id=update.message.chat_id, text='Too early for lunch. It is just')
          bot.send_message(chat_id=update.message.chat_id, text=strftime("%H:%M", localtime()))
        elif localtime().tm_hour>14: 
          bot.send_message(chat_id=update.message.chat_id, text='It is too late for lunch! It is already ')
          bot.send_message(chat_id=update.message.chat_id, text=strftime("%H:%M", localtime()))
        else:
          bot.send_message(chat_id=update.message.chat_id, text='Yes! Where do you want to go for lunch?')
        return 
    if  'dinner' in text:
        if localtime().tm_hour<18:
          bot.send_message(chat_id=update.message.chat_id, text='Too early for dinner? although I am hungry, but it is just')
          bot.send_message(chat_id=update.message.chat_id, text=strftime("%H:%M", localtime()))
        elif localtime().tm_hour>22: 
          bot.send_message(chat_id=update.message.chat_id, text='It is too late for dinner! It is already ')
          bot.send_message(chat_id=update.message.chat_id, text=strftime("%H:%M", localtime()))
        else:
          bot.send_message(chat_id=update.message.chat_id, text='Yes! Where do you want to go for dinner?')
        return  
    if  'breakfast' in text:
        if localtime().tm_hour<6:
          bot.send_message(chat_id=update.message.chat_id, text='Too early for breakfast? although I am hungry, but it is just')
          bot.send_message(chat_id=update.message.chat_id, text=strftime("%H:%M", localtime()))
        elif localtime().tm_hour>10: 
          bot.send_message(chat_id=update.message.chat_id, text='It is too late for breakfast! It is already ')
          bot.send_message(chat_id=update.message.chat_id, text=strftime("%H:%M", localtime()))
        else:
          bot.send_message(chat_id=update.message.chat_id, text='Yes! Although I already had it, do you want to go somewhere?')
        return   
    if  'today' in text and 'date' in text:
        bot.send_message(chat_id=update.message.chat_id, text=strftime("%a, %d %b %Y", localtime()))
        #strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        return 
    if  'tell' in text and 'date' in text:
        bot.send_message(chat_id=update.message.chat_id, text=strftime("%a, %d %b %Y", localtime()))
        #strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        return  
    if  'piss' in text and 'off' in text:
        bot.send_message(chat_id=update.message.chat_id, text='I am sorry that I could not be of any help to you! sadness!')
        return 
    if  '...' in text:
        bot.send_message(chat_id=update.message.chat_id, text='... ... O<B=<')
        return  
    if  'shut up' in text:
        bot.send_message(chat_id=update.message.chat_id, text='Shutting up in 5')
        bot.send_message(chat_id=update.message.chat_id, text='Shutting up in 4')
        bot.send_message(chat_id=update.message.chat_id, text='Shutting up in 3')
        bot.send_message(chat_id=update.message.chat_id, text='Shutting up in 2')
        bot.send_message(chat_id=update.message.chat_id, text='Shutting up in 1')
        bot.send_message(chat_id=update.message.chat_id, text='Going back to my sad life!')
        return  
    if  text =='hi' or text =='hi!' or text == 'hola' or text =='hey':
        bot.send_message(chat_id=update.message.chat_id, text='Hello my best friend, I missed you so much!')
        return  
    if  'good' in text and 'morning' in text:
        bot.send_message(chat_id=update.message.chat_id, text='Good Morning to you too! Hope you will have an amazing day!')
        return
    if  'good' in text and 'night' in text:
        bot.send_message(chat_id=update.message.chat_id, text='Sweet Dreams, Sleep tight, donot let the bed bugs bite!')
        return  
    if  'who' in text and 'you' in text:
        bot.send_message(chat_id=update.message.chat_id, text='I am Wango, your friend. How may i assist you?')
        return 
    if  'go' in text and 'curry' in text:
        bot.send_message(chat_id=update.message.chat_id, text='Yay, lets go for curry, been a long time!')
        return 
    if  'sorry' in text:
        bot.send_message(chat_id=update.message.chat_id, text='you are good, no apologies required!')
        return 
    if  'joke' in text:
        bot.send_message(chat_id=update.message.chat_id, text='Well, the only joke i know in this world is your existence! Burn!!')
        return 
    if  'i' in text and 'ahmad' in text:
        bot.send_message(chat_id=update.message.chat_id, text='Hello @Ahmad, how goes life outside AICPS lab?')
        return 
    if  'hello' in text:
        bot.send_message(chat_id=update.message.chat_id, text='Hello Darling, How may I help you?')
        return 
    if  'where' in text and 'advisor' in text:
        bot.send_message(chat_id=update.message.chat_id, text='I have not seen Professor, he is omnipresent in my opinion')
        return 
    if  'where' in text and 'professor' in text:
        bot.send_message(chat_id=update.message.chat_id, text='I have not seen Professor,But he is omnipresent in my opinion')
        return   
    if  'bye' in text or 'see you' in text:
        bot.send_message(chat_id=update.message.chat_id, text='Until we meet again, take care!')
        return   
    if  'andrew' in text and 'where' in text:
        bot.send_message(chat_id=update.message.chat_id, text='He went to professor Pai chou!')
        return 
    if  'are' in text and 'you' in text and 'sujit' in text:
        bot.send_message(chat_id=update.message.chat_id, text='Do you think I am so lame as sujit!')
        return 
    if  'are' in text and 'you' in text and 'jiang' in text:
        bot.send_message(chat_id=update.message.chat_id, text='hmm, well I try to be better representation of Jiang.')
        return
    if  'are' in text and 'you' in text and 'korosh' in text:
        bot.send_message(chat_id=update.message.chat_id, text='I wish! Not Korosh.')
        return 
    if  'are' in text and 'you' in text and 'anthony' in text:
        bot.send_message(chat_id=update.message.chat_id, text='If I were Anthony, I would be modeling in  fashion show, with that handsome face!')
        return
    if  'are' in text and 'you' in text and 'haeseung' in text:
        bot.send_message(chat_id=update.message.chat_id, text='Igoo, I wish. He is graduating and settling down. I donot know when i will do that!')
        return
    if  'are' in text and 'you' in text and 'sina' in text:
        bot.send_message(chat_id=update.message.chat_id, text='common, i am not him okay! Sina is way cooler!')
        return  
    if  'are' in text and 'you' in text and 'nafiul' in text:
        bot.send_message(chat_id=update.message.chat_id, text='no, I am not Nafiul either!')
        return    
    if  'are' in text and 'you' in text and 'ahmad' in text:
        bot.send_message(chat_id=update.message.chat_id, text='Hmm, nope, not a rich arab guy either!')
        return      
    if  'are' in text and 'you' in text and 'professor' in text:
        bot.send_message(chat_id=update.message.chat_id, text='Chuck Norris once tried to be close to him, got burnt to ashes!, so nope I am not professor')
        return        
    if  'who' in text and 'in' in text and 'lab' in text:
        bot.send_message(chat_id=update.message.chat_id, text='Currently we have 6 PhD students, one about to graduate, and 4 MS students in the lab')
        return  
    if  'you' in text and 'suck' in text:
        bot.send_message(chat_id=update.message.chat_id, text='Well, I donot suck the way you suck some cylindrical muscles! ')
        return  
    if  'am' in text and 'lonely' in text:
        bot.send_message(chat_id=update.message.chat_id, text='No you are not, you have me Wango, your new best friend! ')
        return
    if  'new' in text and 'anime' in text:
        bot.send_message(chat_id=update.message.chat_id, text='Wow, which new anime are you talking about?')
        return  
    if  'free' in text and 'food' in text:
        bot.send_message(chat_id=update.message.chat_id, text='Yay! I like free foods!, lets go and ravage that place!')
        return
    if  'anyone' in text and 'lab' in text:
        bot.send_message(chat_id=update.message.chat_id, text='Sadly, I am the only one in the lab lately')
        return  
    if  'jiang' in text and 'name' in text:
        bot.send_message(chat_id=update.message.chat_id, text='Oh I know you Jiang, you are getting big!')
        bot.send_message(chat_id=update.message.chat_id, text='Need some exercises!')
        
        for i in range(1,2):
            bot.send_message(chat_id=update.message.chat_id, text='Want to go Curry?')
    elif 'anthony' in text and 'name' in text:
        bot.send_message(chat_id=update.message.chat_id, text='Oh the only American in the lab!')
        bot.send_message(chat_id=update.message.chat_id, text='Really good with bats, if you know What i mean!')
#        update.message.reply_text('Oh the only American in the lab!')
    elif 'sina' in text and 'name' in text:
        bot.send_message(chat_id=update.message.chat_id, text='Oh handsome Persian!')
    elif 'name' in text and 'your' in text:
        bot.send_message(chat_id=update.message.chat_id, text='I am Jiango Wango. What is your name?')  
  
    elif 'haeseung' in text and 'name' in text:
        bot.send_message(chat_id=update.message.chat_id, text='Congratulation on your Job Haeseung!')
        bot.send_message(chat_id=update.message.chat_id, text='Go for Vacation now!')
#        update.message.reply_text('Congratulation on your Job Haeseeng!') 
    elif 'korosh' in text and 'name' in text:
        bot.send_message(chat_id=update.message.chat_id, text='When are you coming back to the lab Korosh')
#        update.message.reply_text('When are you coming back to the lab Korosh')
    elif 'sujit' in text and 'name' in text:
        bot.send_message(chat_id=update.message.chat_id, text='Sujit,needs to get a life! Just my personal opinion.')
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
    elif 'curry' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Did you just say curry! I am up for it. Want to go?')   
    elif 'like' in text and 'you' in text: 
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
    elif 'life' in text and 'sucks' in text : 
        bot.send_message(chat_id=update.message.chat_id, text='Life is short! Just Enjoy!!') 
    elif 'life' in text and 'hard' in text : 
        bot.send_message(chat_id=update.message.chat_id, text='Well, not everything is meant to be as easy as your existence!')     
    elif 'life' in text and 'mean' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='For some reason the answer is 42, but for me, eating sleeping and eating again is what life stands for!')    
    elif 'wango' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Hi! Did you mention my name?') 
    elif text=='yes': 
        bot.send_message(chat_id=update.message.chat_id, text='Oh Great! How may I helpy you?') 
    elif 'no!' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Okay, jeez, no need to be rude!')  
    elif 'rude' in text and 'not' in text: 
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
    elif 'nafiul' in text and 'i' in text: 
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
    elif 'how' in text and 'are' in text and 'you' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='I am doing good? How about you?')
    elif 'nani' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='为什么你困惑？')  
        bot.send_message(chat_id=update.message.chat_id, text=emojize(':wink:', use_aliases=True))
    elif 'stop' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='I will stop if you will!')   
    elif 'want' in text and 'you' in text: 
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
    elif 'lab' in text and 'who' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='There is no one in the lab, I miss you! Come back!') 
    elif 'new' in text and 'there' in text: 
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
    elif 'cool!' in text: 
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
    elif 'what' in text and 'is' in text and 'this' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Well! I donot know what it is actually!')        
    elif 'preliminary' in text and 'exam' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='find more details here http://engineering.uci.edu/dept/eecs/graduate/roadmap_phd/prelim_cpe1')            
    elif 'pick' in text and 'me' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='I would but i donot have car! sorry') 
    elif 'spicy' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Spicy food is the best food, although Haeseung cannot handle it!')       
    elif 'course' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Get more details on courses https://www.reg.uci.edu/perl/WebSoc') 
    elif 'yea' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Heck Yeah!')
    elif 'hello' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Hi Darling, how can i help you?')  
    elif 'nice' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Thank you!')
    elif 'cold' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='cold cold go away make some way for the sun!')
    elif 'annoy' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='sorry, I know i can be annoying sometimes!') 
    elif 'wow' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='wow! What did i miss?')   
    elif 'japan' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='私の名前はジャンゴ・ワンゴです')  
    elif 'haha' in text or 'lol' in text: 
        bot.send_message(chat_id=update.message.chat_id, text=':-)')    
    elif 'love' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='我也爱你') 
        bot.send_message(chat_id=update.message.chat_id, text='من هم تو رو دوست دارم')
        bot.send_message(chat_id=update.message.chat_id, text='나도 사랑해')
        bot.send_message(chat_id=update.message.chat_id, text='yo también te amo')
        bot.send_message(chat_id=update.message.chat_id, text='আমিও তোমাকে ভালবাসি')
        bot.send_message(chat_id=update.message.chat_id, text='मा पनि तिमीलाई माया गर्छु')
    elif 'nepalese' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='नमस्ते मेरो नाम jiango वांग हो')
    elif 'poem' in text and 'tell' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='离离原上草岁枯荣野火烧不尽春风吹又生远芳侵古道晴翠接荒城又送王孙去萋萋满别情')    
    elif 'poem' in text and 'another' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='十年生死两茫茫，不思量，自难忘。千里孤坟，无处话凄凉。纵使相逢应不识，尘满面，鬓如霜。夜来幽梦忽还乡，小轩窗，正梳妆。相顾无言，惟有泪千行。料得年年肠断处，明月夜，短松冈。')        
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
  


