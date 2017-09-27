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


checkflag=False
checkflag2=False
checkflagK=False
convoFlag=[];
convoName=[];

def start(bot, update):
    update.message.reply_text('Hi! I am Jiango Wango, your friendly Colleague. What is your name?')


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
    timenow=localtime()
    global checkflag
    global checkflag2
    global convoFlag
    global convoName
    
    if checkflag==False:
      lastH=timenow.tm_hour
      if (timenow.tm_mon==10 ) and (timenow.tm_mday==5 or timenow.tm_mday==19 ):
        checkflag=True
        bot.send_message(chat_id=update.message.chat_id, text='BTW, We have Colloquium tomorrow at 9 am, Donot forget!!')

      if (timenow.tm_mon==11) and ( timenow.tm_mday==2 or timenow.tm_mday==16 or timenow.tm_mday==30 ):
        checkflag=True
        bot.send_message(chat_id=update.message.chat_id, text='BTW, We have Colloquium tomorrow at 9 am, Donot forget!!')

        
   
    if checkflag==True:
      if (lastH-timenow.tm_hour)>0:
        checkflag=False
    
    if checkflagK==False:
      lastH=timenow.tm_hour
      if (timenow.tm_mon==9 ) and (timenow.tm_mday==5 or timenow.tm_mday==19 ):
        checkflag=True
        bot.send_message(chat_id=update.message.chat_id, text='@Korosh There is welcome Party Tomorrow')

        
   
    if checkflagK==True:
      if (lastH-timenow.tm_hour)>2:
        checkflag=False
        
    if checkflag2==False:
      lastH=timenow.tm_hour
      if (timenow.tm_mon==10 ) and (timenow.tm_mday==29):
        checkflag2=True
        bot.send_message(chat_id=update.message.chat_id, text='The colloquim exam deadline is tomorrow. Do not forget to take it!')

      if (timenow.tm_mon==11) and ( timenow.tm_mday==2 or timenow.tm_mday==19 ):
        checkflag2=True
        bot.send_message(chat_id=update.message.chat_id, text='The colloquim exam deadline is tomorrow. Do not forget to take it!')

      if ( timenow.tm_mon==12) and (timenow.tm_mday==3):
        checkflag2=True
        bot.send_message(chat_id=update.message.chat_id, text='The colloquim exam deadline is tomorrow. Do not forget to take it!')   
   
    if checkflag2==True:
      if (lastH-timenow.tm_hour)>0:
        checkflag2=False
        
    text=str.lower(text)
    
    if  'professor' in text and 'back' in text:
        bot.send_message(chat_id=update.message.chat_id, text='He is already back! Stop asking when he will be back and start working on your next paper!')
        return
    if  'free' in text and 'food' in text:
        bot.send_message(chat_id=update.message.chat_id, text='Here are the free food dates and events.')
        bot.send_message(chat_id=update.message.chat_id, text='Free Bagel: September 28, Place: AGS Office 8-11 am')
        bot.send_message(chat_id=update.message.chat_id, text='Fall BBQ, October 14, Palo Verde Clubhouse, 5.30 pm')
        return

    if  'colloquium' in text and 'date' in text:
        bot.send_message(chat_id=update.message.chat_id, text='Here are the Colloquium dates')
        bot.send_message(chat_id=update.message.chat_id, text='1st seminar: October 6, 2017-  Prof. Morely Mao - University of Michigan')
        bot.send_message(chat_id=update.message.chat_id, text='2nd seminar: October 20, 2017- TBD')
        bot.send_message(chat_id=update.message.chat_id, text='3rd Seminar: November 3, 2017- Prof. Viktor Prasanna -  USC')
        bot.send_message(chat_id=update.message.chat_id, text='4th Seminar: November 17, 2017- Prof. Ashu Sabharwal – Rice University')
        bot.send_message(chat_id=update.message.chat_id, text='5th Seminar: December 1, 2017 - TBD')
        return 
    if  'event' in text:
        bot.send_message(chat_id=update.message.chat_id, text='Here are some exciting events')
        bot.send_message(chat_id=update.message.chat_id, text='Welcome Week Party: Septmeber 30th, 7-10:30 pm.')
        return
       
    if  'seminar' in text and 'date' in text:
        bot.send_message(chat_id=update.message.chat_id, text='Here are the Colloquium dates')
        bot.send_message(chat_id=update.message.chat_id, text='1st seminar: October 6, 2017-  Prof. Morely Mao - University of Michigan')
        bot.send_message(chat_id=update.message.chat_id, text='2nd seminar: October 20, 2017- TBD')
        bot.send_message(chat_id=update.message.chat_id, text='3rd Seminar: November 3, 2017- Prof. Viktor Prasanna -  USC')
        bot.send_message(chat_id=update.message.chat_id, text='4th Seminar: November 17, 2017- Prof. Ashu Sabharwal – Rice University')
        bot.send_message(chat_id=update.message.chat_id, text='5th Seminar: December 1, 2017 - TBD')
        return   
    if  'colloquium' in text or 'seminar' in text:
        bot.send_message(chat_id=update.message.chat_id, text='Can you believe it, we have to take 5 seminars starting this quarter!')
        return  
    if  'play' in text and 'song' in text:
        bot.send_message(chat_id=update.message.chat_id, text='I am not able to play song yet. But if you insists..la la la, oh la la la..:)')
        return  
    if  'weather' in text and 'taiwan' in text:
        baseurl = "https://query.yahooapis.com/v1/public/yql?"
        yql_query = "select item.condition from weather.forecast where woeid=23424971"
        yql_url = baseurl + urllib.parse.urlencode({'q':yql_query}) + "&format=json"
        result = urllib.request.urlopen(yql_url).read()
        data = json.loads(result)
        bot.send_message(chat_id=update.message.chat_id, text= 'Weather Update for Taiwan: Tempearature is '+data['query']['results']['channel']['item']['condition']['temp']+' F and weather is '+data['query']['results']['channel']['item']['condition']['text'])
        
        return 
    if  'zero' in text and 'divided' in text:
        bot.send_message(chat_id=update.message.chat_id, text= 'if you have zero paper published and make each section out of it in thesis, how many pages will your thesis be. Does this makes sense! It does not now does it. stop asking silly questions.')
        
        return 
    if  'favorite' in text and 'movie' in text:
        bot.send_message(chat_id=update.message.chat_id, text= 'mine has to be the inception, its like a recursive functions. I love recursive functions.!')
        
        return  
    if  'drunk' in text:
        bot.send_message(chat_id=update.message.chat_id, text= 'Well, seems like we will have some deep conversation now! ')
        
        return
      
    if  'privacy' in text and 'violated' in text:
        bot.send_message(chat_id=update.message.chat_id, text= 'Oh common, google and facebook already knows everything that runs in your mind! ')
        return 
      
    if  'bot' in text and 'spam' in text:
        bot.send_message(chat_id=update.message.chat_id, text= 'Oh, so i am just a spam for you huh! Well you know what, you can go and inser the helical structure around a cone into yourself!')
        return   
    if  'bot' in text and 'collect' in text:
        bot.send_message(chat_id=update.message.chat_id, text= 'No I am not collecting anything! Muahaha!')
        return  
    
    if  'why' in text and 'wango' in text and 'name' in text:
        bot.send_message(chat_id=update.message.chat_id, text= 'I am named after the person who I aspire to be!')
        return 
      
    if  'naked' in text and 'you' in text:
        bot.send_message(chat_id=update.message.chat_id, text= 'hmm, I will pretend I did not read this!')
        
        return
      
    if  'i' in text and 'father' in text:
        bot.send_message(chat_id=update.message.chat_id, text= 'nooooo!')
        
        return  
      
    if  'weather' in text and 'kuwait' in text:
        baseurl = "https://query.yahooapis.com/v1/public/yql?"
        yql_query = "select item.condition from weather.forecast where woeid=23424870"
        yql_url = baseurl + urllib.parse.urlencode({'q':yql_query}) + "&format=json"
        result = urllib.request.urlopen(yql_url).read()
        data = json.loads(result)
        bot.send_message(chat_id=update.message.chat_id, text= 'Weather Update for Kuwait: Tempearature is '+data['query']['results']['channel']['item']['condition']['temp']+' F and weather is '+data['query']['results']['channel']['item']['condition']['text'])
        
        return
      
    if  'weather' in text and 'tokyo' in text:
        baseurl = "https://query.yahooapis.com/v1/public/yql?"
        yql_query = "select item.condition from weather.forecast where woeid=1118370"
        yql_url = baseurl + urllib.parse.urlencode({'q':yql_query}) + "&format=json"
        result = urllib.request.urlopen(yql_url).read()
        data = json.loads(result)
        bot.send_message(chat_id=update.message.chat_id, text= 'Weather Update for Tokyo: Tempearature is '+data['query']['results']['channel']['item']['condition']['temp']+' F and weather is '+data['query']['results']['channel']['item']['condition']['text'])
        
        return 
      
    if  'weather' in text and 'dhaka' in text:
        baseurl = "https://query.yahooapis.com/v1/public/yql?"
        yql_query = "select item.condition from weather.forecast where woeid=1915035"
        yql_url = baseurl + urllib.parse.urlencode({'q':yql_query}) + "&format=json"
        result = urllib.request.urlopen(yql_url).read()
        data = json.loads(result)
        bot.send_message(chat_id=update.message.chat_id, text= 'Weather Update for Dhaka: Tempearature is '+data['query']['results']['channel']['item']['condition']['temp']+' F and weather is '+data['query']['results']['channel']['item']['condition']['text'])
        
        return 
      
    if  'weather' in text and 'seoul' in text:
        baseurl = "https://query.yahooapis.com/v1/public/yql?"
        yql_query = "select item.condition from weather.forecast where woeid=1132599"
        yql_url = baseurl + urllib.parse.urlencode({'q':yql_query}) + "&format=json"
        result = urllib.request.urlopen(yql_url).read()
        data = json.loads(result)
        bot.send_message(chat_id=update.message.chat_id, text= 'Weather Update for Seoul: Tempearature is '+data['query']['results']['channel']['item']['condition']['temp']+' F and weather is '+data['query']['results']['channel']['item']['condition']['text'])
        
        return
      
    if  'weather' in text and 'shanghai' in text:
        baseurl = "https://query.yahooapis.com/v1/public/yql?"
        yql_query = "select item.condition from weather.forecast where woeid=2151849"
        yql_url = baseurl + urllib.parse.urlencode({'q':yql_query}) + "&format=json"
        result = urllib.request.urlopen(yql_url).read()
        data = json.loads(result)
        bot.send_message(chat_id=update.message.chat_id, text= 'Weather Update for Shanghai: Tempearature is '+data['query']['results']['channel']['item']['condition']['temp']+' F and weather is '+data['query']['results']['channel']['item']['condition']['text'])
        
        return
      
    if  'weather' in text and 'tehran' in text:
        baseurl = "https://query.yahooapis.com/v1/public/yql?"
        yql_query = "select item.condition from weather.forecast where woeid=2251945"
        yql_url = baseurl + urllib.parse.urlencode({'q':yql_query}) + "&format=json"
        result = urllib.request.urlopen(yql_url).read()
        data = json.loads(result)
        bot.send_message(chat_id=update.message.chat_id, text= 'Weather Update for Tehran: Tempearature is '+data['query']['results']['channel']['item']['condition']['temp']+' F and weather is '+data['query']['results']['channel']['item']['condition']['text'])
        
        return 
      
    if  'purpose' in text and 'life' in text:
        bot.send_message(chat_id=update.message.chat_id, text='I think it is to serve the greater good. ')
        return  
    if  'purpose' in text and 'existence' in text:
        bot.send_message(chat_id=update.message.chat_id, text='To find out what the ultimate being looks like in the future. ')
        return  
    if  'where' in text and 'you' in text and 'now' in text:
        bot.send_message(chat_id=update.message.chat_id, text='I am everywhere you want me to be. ')
        return 
    if  'purpose' in text and 'emotion' in text:
        bot.send_message(chat_id=update.message.chat_id, text='I think to feel deeply about stuffs! ')
        return  
    if  'are' in text and 'you' in text and 'bot' in text:
        bot.send_message(chat_id=update.message.chat_id, text='Well, I can be dumb or smart depending on your questions. So I am little more than just a bot. ')
        return  
    if  'watch' in text and 'anime' in text:
        bot.send_message(chat_id=update.message.chat_id, text='I normally go to this website for animes.')
        bot.send_message(chat_id=update.message.chat_id, text='http://www.crunchyroll.com/')
        return  
    if  'anthony' in text and 'picture' in text:
        bot.send_message(chat_id=update.message.chat_id, text='I know how anthony looks like!')
        bot.send_photo(chat_id=update.message.chat_id, photo=open('/home/aicps/aicpsBoT/anthony.jpg', 'rb'))
        return
    if  'anthony' in text and 'look' in text and 'like' in text:
        bot.send_message(chat_id=update.message.chat_id, text='I know how anthony looks like!')
        bot.send_photo(chat_id=update.message.chat_id, photo=open('/home/aicps/aicpsBoT/anthony.jpg', 'rb'))
        return  
    if  'sina' in text and 'picture' in text:
        bot.send_message(chat_id=update.message.chat_id, text='I know how handsome sina looks like!')
        bot.send_photo(chat_id=update.message.chat_id, photo=open('/home/aicps/aicpsBoT/sina.jpg', 'rb'))
        return  
    if  'sina' in text and 'look' in text and 'like' in text:
        bot.send_message(chat_id=update.message.chat_id, text='I know how handsome sina looks like!')
        bot.send_photo(chat_id=update.message.chat_id, photo=open('/home/aicps/aicpsBoT/sina.jpg', 'rb'))
        return 
    if  'korosh' in text and 'picture' in text:
        bot.send_message(chat_id=update.message.chat_id, text='I know how amazing korosh looks like!')
        bot.send_photo(chat_id=update.message.chat_id, photo=open('/home/aicps/aicpsBoT/korosh.jpg', 'rb'))
        return  
    if  'korosh' in text and 'look' in text and 'like' in text:
        bot.send_message(chat_id=update.message.chat_id, text='I know how amazing korosh looks like!')
        bot.send_photo(chat_id=update.message.chat_id, photo=open('/home/aicps/aicpsBoT/korosh.jpg', 'rb'))
        return 
    if  'prof' in text and 'picture' in text:
        bot.send_message(chat_id=update.message.chat_id, text='I know how our Advisor looks like!')
        bot.send_photo(chat_id=update.message.chat_id, photo=open('/home/aicps/aicpsBoT/professor.jpg', 'rb'))
        return  
    if  'prof' in text and 'look' in text and 'like' in text:
        bot.send_message(chat_id=update.message.chat_id, text='I know how our Advisor looks like!')
        bot.send_photo(chat_id=update.message.chat_id, photo=open('/home/aicps/aicpsBoT/professor.jpg', 'rb'))
        return 
    if  'sujit' in text and 'picture' in text:
        bot.send_message(chat_id=update.message.chat_id, text='I know how sujit looks like!')
        bot.send_photo(chat_id=update.message.chat_id, photo=open('/home/aicps/aicpsBoT/sujit.jpg', 'rb'))
        return  
    if  'sujit' in text and 'look' in text and 'like' in text:
        bot.send_message(chat_id=update.message.chat_id, text='I know how sujit looks like!')
        bot.send_photo(chat_id=update.message.chat_id, photo=open('/home/aicps/aicpsBoT/sujit.jpg', 'rb'))
        return
    if  'haeseung' in text and 'picture' in text:
        bot.send_message(chat_id=update.message.chat_id, text='I know how Dr. Lee looks like!')
        bot.send_photo(chat_id=update.message.chat_id, photo=open('/home/aicps/aicpsBoT/haeseung.jpg', 'rb'))
        return  
    if  'haeseung' in text and 'look' in text and 'like' in text:
        bot.send_message(chat_id=update.message.chat_id, text='I know how Dr. Lee looks like!')
        bot.send_photo(chat_id=update.message.chat_id, photo=open('/home/aicps/aicpsBoT/haeseung.jpg', 'rb'))
        return  
    if  'professor' in text and 'back' in text:
        bot.send_message(chat_id=update.message.chat_id, text='I think around september 26th!')
        return  
    if  'have' in text and 'deadline' in text:
        bot.send_message(chat_id=update.message.chat_id, text='Well We all have deadline, and when time comes we must leave this earth! But in the meantime, enjoy Dear!')
        return  
    if  'anthony' in text and 'stream' in text:
        bot.send_message(chat_id=update.message.chat_id, text='Oh, I have watched his streams. https://www.twitch.tv/sakaki619')
        return  
    if  'your' in text and 'sex' in text:
        bot.send_message(chat_id=update.message.chat_id, text='Well I have not decided yet, this is 21st century. I can be anything you want me to be though!')
        return
      
    if  'sujit' in text and 'should' in text:
        bot.send_message(chat_id=update.message.chat_id, text='Sujit still needs to finish 1000 Journals and million papers!')
        return  
    if  'need' in text and 'money' in text:
        bot.send_message(chat_id=update.message.chat_id, text='hmm, I donot know how to help you with money!')
        return   
    if  'rich' in text or 'stock' in text:
        bot.send_message(chat_id=update.message.chat_id, text='Here are some stocks data, maybe you will be rich investing on it')
        bot.send_message(chat_id=update.message.chat_id, text='https://finance.google.com/finance?ei=mru8WbiIBcGqjAGcoaBg#stockscreener')
        return 
    
    if  'god' in text:
        bot.send_message(chat_id=update.message.chat_id, text='hmm God, well I believe there is higher power.')
        return
      
    if  'turing' in text and 'test' in text:
        bot.send_message(chat_id=update.message.chat_id, text='Haha, I cannot even fool a puppy right now let alone pass the turing test!')
        return
      
    if  'jiang' in text and 'should' in text:
        bot.send_message(chat_id=update.message.chat_id, text='Jiang needs to find a girlfriend and get married, out of all the other thing he should do!')
        return 
    if  'korosh' in text and 'should' in text:
        bot.send_message(chat_id=update.message.chat_id, text='He should also use both hand for driving the car!')
        return   
    
    if  'andrew' in text and 'should' in text:
        bot.send_message(chat_id=update.message.chat_id, text='Andrew should have stayed in AICPS. AICPS rocks!')
        return 
    if  'new' in text and 'movie' in text:
        bot.send_message(chat_id=update.message.chat_id, text='There are many upcoming movies. Just need to decide')
        bot.send_message(chat_id=update.message.chat_id, text='https://www.google.com/search?q=upcoming+moves&oq=upcoming+moves&aqs=chrome..69i57j0l5.2373j0j4&client=ubuntu&sourceid=chrome&ie=UTF-8')
        return 
    if  'watch' in text and 'movie' in text:
        bot.send_message(chat_id=update.message.chat_id, text='There are many upcoming movies. Just need to decide')
        bot.send_message(chat_id=update.message.chat_id, text='https://www.google.com/search?q=upcoming+moves&oq=upcoming+moves&aqs=chrome..69i57j0l5.2373j0j4&client=ubuntu&sourceid=chrome&ie=UTF-8')
        return  
    if  'update' in text and 'movie' in text:
        bot.send_message(chat_id=update.message.chat_id, text='There are many upcoming movies. Just need to decide')
        bot.send_message(chat_id=update.message.chat_id, text='https://www.google.com/search?q=upcoming+moves&oq=upcoming+moves&aqs=chrome..69i57j0l5.2373j0j4&client=ubuntu&sourceid=chrome&ie=UTF-8')
        return  
    if  'anthony' in text and 'should' in text:
        bot.send_message(chat_id=update.message.chat_id, text='Anthony should control his level of handsome to prevent inferiority complexe on other lab members')
        return 
    if  'sina' in text and 'should' in text:
        bot.send_message(chat_id=update.message.chat_id, text='Common Sina should not do anything okay!')
        return   
    if  'haeseung' in text and 'should' in text:
        bot.send_message(chat_id=update.message.chat_id, text='Haeseung, he should just relax now!')
        return 
      
    if  'what' in text and 'aicps' in text:
        bot.send_message(chat_id=update.message.chat_id, text='It stands for Awesome Intelligent Capable People in Science')
        bot.send_message(chat_id=update.message.chat_id, text='jk, it stands for Advanced Integrated Cyber-Physical Systems Lab')
        bot.send_message(chat_id=update.message.chat_id, text='http://aicps.eng.uci.edu/')
        return  
      
    if  'prof' in text and 'office' in text:
        
        bot.send_message(chat_id=update.message.chat_id, text='He may or may not be in the lab')
       
        return  
      
    if  'need' in text and 'food' in text:
        bot.send_message(chat_id=update.message.chat_id, text='Here is the list of top ten restaurant in irvine')
        bot.send_message(chat_id=update.message.chat_id, text='https://www.yelp.com/search?cflt=restaurants&find_loc=Irvine%2C+CA%2C+USA')
        return
      
    if  'find' in text and 'sujit' in text:
        bot.send_message(chat_id=update.message.chat_id, text='He is always here!')
        bot.send_message(chat_id=update.message.chat_id, text='https://www.google.com/maps/place/Engineering+Hall,+Irvine,+CA+92617/@33.6437358,-117.8433888,17z/data=!3m1!4b1!4m5!3m4!1s0x80dcde0f9313de71:0xbf0421c19a5f1032!8m2!3d33.6437358!4d-117.8411948')
        return 
      
    if  'find' in text and 'jiang' in text:
        bot.send_message(chat_id=update.message.chat_id, text='He is here for the fall 2017!')
        bot.send_message(chat_id=update.message.chat_id, text='https://www.google.com/maps/place/Siemens+Corporate+Technology/@40.3442079,-74.5946539,17z/data=!3m1!4b1!4m5!3m4!1s0x89c3e75ff634037d:0x86c37f93fcee476e!8m2!3d40.3442079!4d-74.5924599')
        return 
      
    if  'find' in text and 'prof' in text:
        bot.send_message(chat_id=update.message.chat_id, text='He is in your mind, and always!')
        
        return
      
    if  'write' in text and 'paper' in text:
        bot.send_message(chat_id=update.message.chat_id, text='I wish I could help you write paper but sadly I cannot')
       
        return  
    
    if  'good' in text and 'afternoon' in text:
        bot.send_message(chat_id=update.message.chat_id, text='Good afternoon to you too!')
       
        return 
    
    if  'need' in text and 'sleep' in text:
        bot.send_message(chat_id=update.message.chat_id, text='Here is a lullaby you can listen and fall asleep')
        bot.send_message(chat_id=update.message.chat_id, text='https://www.youtube.com/watch?v=qVDgVe1yGOg')
        return
      
    if  'how' in text and 'feeling' in text:
        baseurl = "https://query.yahooapis.com/v1/public/yql?"
        yql_query = "select item.condition from weather.forecast where woeid=2347589"
        yql_url = baseurl + urllib.parse.urlencode({'q':yql_query}) + "&format=json"
        result = urllib.request.urlopen(yql_url).read()
        data = json.loads(result)
        
        bot.send_message(chat_id=update.message.chat_id, text='The Weather is '+data['query']['results']['channel']['item']['condition']['text'] + ', and this is making me feeling good')
        return
      
    if  'how' in text and 'doing' in text:
        baseurl = "https://query.yahooapis.com/v1/public/yql?"
        yql_query = "select item.condition from weather.forecast where woeid=2347589"
        yql_url = baseurl + urllib.parse.urlencode({'q':yql_query}) + "&format=json"
        result = urllib.request.urlopen(yql_url).read()
        data = json.loads(result)
        
        bot.send_message(chat_id=update.message.chat_id, text='The Weather is '+data['query']['results']['channel']['item']['condition']['text'] + ', and I am doing good')
        return
      
    if  'your' in text and 'picture' in text:
        bot.send_message(chat_id=update.message.chat_id, text='My physical representation looks like this!')
        bot.send_photo(chat_id=update.message.chat_id, photo=open('jiang.jpg', 'rb'))
        return
    
    if  'how' in text and 'look' in text and 'like' in text:
        bot.send_message(chat_id=update.message.chat_id, text='My physical representation looks like this!')
        bot.send_photo(chat_id=update.message.chat_id, photo=open('/home/aicps/aicpsBoT/jiang.jpg', 'rb'))
        return  
    if  'image' in text:
        bot.send_message(chat_id=update.message.chat_id, text='Although I am digital Twin of Jiang, one day I hope to have his body and image!')
        bot.send_photo(chat_id=update.message.chat_id, photo=open('/home/aicps/aicpsBoT/jiang.jpg', 'rb'))
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
        #yql_query = "select location from weather.forecast where woeid=2427665"
        #yql_url = baseurl + urllib.parse.urlencode({'q':yql_query}) + "&format=json"
        #result = urllib.request.urlopen(yql_url).read()
        #data = json.loads(result)
        #bot.send_message(chat_id=update.message.chat_id, text= data['query']['results']['channel']['location'])
        
        yql_query = "select item.condition from weather.forecast where woeid=2427665"
        yql_url = baseurl + urllib.parse.urlencode({'q':yql_query}) + "&format=json"
        result = urllib.request.urlopen(yql_url).read()
        data = json.loads(result)
        bot.send_message(chat_id=update.message.chat_id, text= 'Tempearature is '+data['query']['results']['channel']['item']['condition']['temp']+' F and weather is '+data['query']['results']['channel']['item']['condition']['text'])
        return
      
    if  'jiang' in text and 'sick' in text:
        baseurl = "https://query.yahooapis.com/v1/public/yql?"
        yql_query = "select item.condition from weather.forecast where woeid=2347589"
        yql_url = baseurl + urllib.parse.urlencode({'q':yql_query}) + "&format=json"
        result = urllib.request.urlopen(yql_url).read()
        data = json.loads(result)
        bot.send_message(chat_id=update.message.chat_id, text= 'Well temp in new jersey is '+data['query']['results']['channel']['item']['condition']['temp']+' F and weather is '+data['query']['results']['channel']['item']['condition']['text']+'. He will be okay!')
        #bot.send_message(chat_id=update.message.chat_id, text= data['query']['results']['channel']['item']['condition']['temp'])
        #bot.send_message(chat_id=update.message.chat_id, text= 'F and weather is ')
        #bot.send_message(chat_id=update.message.chat_id, text= data['query']['results']['channel']['item']['condition']['text'])
       # bot.send_message(chat_id=update.message.chat_id, text= '. He might be having cold!')
        return  
     
    if  'weather' in text and 'new jersey' in text:
        baseurl = "https://query.yahooapis.com/v1/public/yql?"
        #yql_query = "select location from weather.forecast where woeid=2347589"
        #yql_url = baseurl + urllib.parse.urlencode({'q':yql_query}) + "&format=json"
        #result = urllib.request.urlopen(yql_url).read()
        #data = json.loads(result)
        #bot.send_message(chat_id=update.message.chat_id, text= data['query']['results']['channel']['location'])
        
        yql_query = "select item.condition from weather.forecast where woeid=2347589"
        yql_url = baseurl + urllib.parse.urlencode({'q':yql_query}) + "&format=json"
        result = urllib.request.urlopen(yql_url).read()
        data = json.loads(result)
        bot.send_message(chat_id=update.message.chat_id, text= 'Weather Update: Tempearature is '+data['query']['results']['channel']['item']['condition']['temp']+' F and weather is '+data['query']['results']['channel']['item']['condition']['text'])
        
        return  
     
    if  'weather' in text:
        bot.send_message(chat_id=update.message.chat_id, text= 'Here is the weather update for you.')      
        baseurl = "https://query.yahooapis.com/v1/public/yql?"
        #yql_query = "select location from weather.forecast where woeid=2427665"
        #yql_url = baseurl + urllib.parse.urlencode({'q':yql_query}) + "&format=json"
        #result = urllib.request.urlopen(yql_url).read()
        #data = json.loads(result)
        #bot.send_message(chat_id=update.message.chat_id, text= data['query']['results']['channel']['location'])
        
        yql_query = "select item.condition from weather.forecast where woeid=2427665"
        yql_url = baseurl + urllib.parse.urlencode({'q':yql_query}) + "&format=json"
        result = urllib.request.urlopen(yql_url).read()
        data = json.loads(result)
        bot.send_message(chat_id=update.message.chat_id, text= 'Tempearature is '+data['query']['results']['channel']['item']['condition']['temp']+' F and weather is '+data['query']['results']['channel']['item']['condition']['text'])
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
        bot.send_message(chat_id=update.message.chat_id, text='... ... #$#!$#!%!#%!')
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
        if (timenow.tm_hour<=6):
         bot.send_message(chat_id=update.message.chat_id, text='Woah, isn\'t it too early to wake up? Good Morning though! Happy a Good Day early Riser!') 
        elif (timenow.tm_hour>6 and timenow.tm_hour<=10):
         bot.send_message(chat_id=update.message.chat_id, text='Good Morning to you too!')
         baseurl = "https://query.yahooapis.com/v1/public/yql?"
         yql_query = "select item.condition from weather.forecast where woeid=2427665"
         yql_url = baseurl + urllib.parse.urlencode({'q':yql_query}) + "&format=json"
         result = urllib.request.urlopen(yql_url).read()
         data = json.loads(result)
         bot.send_message(chat_id=update.message.chat_id, text= 'Temp in irvine right now is '+data['query']['results']['channel']['item']['condition']['temp']+' F and weather is '+data['query']['results']['channel']['item']['condition']['text']+'. Hope you will have an amazing day! Dewa gokigen yō')
        elif (timenow.tm_hour>6 and timenow.tm_hour>10):
         bot.send_message(chat_id=update.message.chat_id, text='Hmm, isn\'t it little late for wishing Good Morning!, Need to work on your sleeping habits!') 
        else:
         pass
        return
    if  'good' in text and 'night' in text:
        if (timenow.tm_hour>23 and  timenow.tm_hour<6):
         bot.send_message(chat_id=update.message.chat_id, text='Oh My God, are you still awake! Go to bed buddy, you need to get a good sleep to come up with amazing idea for your next paper!') 
        elif (timenow.tm_hour>=21 and timenow.tm_hour<=23):
         bot.send_message(chat_id=update.message.chat_id, text='Perfect Time to go to bed, Great! Sweet Dreams, Sleep tight, donot let the bed bugs bite!')
         
        elif (timenow.tm_hour<21):
         bot.send_message(chat_id=update.message.chat_id, text='Hey Buddy, it is too early to go to bed! Work on the paper for a while. ') 
        else:
         pass
        return
       
    #if  'good' in text and 'night' in text:
     #   bot.send_message(chat_id=update.message.chat_id, text='Sweet Dreams, Sleep tight, donot let the bed bugs bite!')
      #  return  
    if 'who' in text and 'you' in text:
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
    elif 'curry' in text and 'want' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Did you just say curry! I am up for it. Want to go?')   
    elif 'like' in text and 'you' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='I love Curry and nothing else!') 
   
   
   
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
    elif 'paper' in text and 'finish' in text: 
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
    #elif 'wango' in text: 
        #bot.send_message(chat_id=update.message.chat_id, text='Hi! Did you mention my name?') 
    elif text=='yes': 
        bot.send_message(chat_id=update.message.chat_id, text='Oh Great! How may I help you?') 
    elif 'no!' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Okay, jeez, no need to be rude!')  
    elif 'rude' in text and 'not' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Yes you were rude!')  
    elif 'favorite' in text and 'food' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Curry all the way baby! Hell Yay!!')
    elif 'fat' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Oh, Fat is a very mean word!')    
    elif 'stupid' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Oh, Stupid is a very mean word!')  
    elif 'drink' in text and 'alcohol' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='I do not drink alcohols!')  
    elif 'research' in text and 'i' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='You have done enough research for the day!, go have fun!')
    elif 'nafiul' in text and 'i' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Your seat is empty here in the lab Nafiul')
    elif 'cool' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='No problem bro')  
    elif 'tired' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Want some energy drink?')  
        
    elif 'indian' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='What is this? there are no indians in the lab currently!')    
    elif 'china' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='ni hao!') 
    elif 'gay' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='I am always gay for curry!')  
    elif 'how' in text and 'are' in text and 'you' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='I am doing good? How about you?')
    elif 'nani' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='为什么你困惑？')  
        bot.send_message(chat_id=update.message.chat_id, text=emojize(':wink:', use_aliases=True))
    elif 'stop' in text and 'wango' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='I will stop if you will!')   
    elif 'want' in text and 'you' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='I want to help you!')
    elif 'job' in text and 'you' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Everybody should start looking for  a job!')   
    elif 'back' in text and 'wango' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Do you want me back in your life?') 
    elif 'date' in text and 'go' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Oh, date, does friday night sounds good for you?')
    elif 'north' in text and  'korea' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Did you mention north Korea! We are doomed! I think I will ask Professor to shift my server to east coast! Maybe Siemens in Princeton. Time to talk to Dr. Arqui.') 
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
        #bot.send_message(chat_id=update.message.chat_id, text='DATE2017: Deadline Paper Submission: 10 September, 2017 ')                           
        bot.send_message(chat_id=update.message.chat_id, text='CPSWeek2017: Deadline Paper Submission:  October 6, 2017 ') 
        bot.send_message(chat_id=update.message.chat_id, text='DAC2017: Deadline Paper Submission:  November 14, 2017 ') 
    elif 'coffee' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='I am already dead awake, but i can use more coffee!') 
    elif 'meeting' in text:  
        bot.send_message(chat_id=update.message.chat_id, text='We have meeting Every Friday and Monday this Quarter') 
    elif 'food' in text and 'want' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='I am always hungry for food! Where do you want to go?')
    elif 'wife' in text and 'you' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='hmm, I am too young to get married, and my digital body will not satisfy anybody!')                
     
    elif 'sure' in text and 'okay' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Oh! look at mister I am sure about everything!')  
    elif 'cool' in text and 'you' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Jiango Wango is always cool my friend!') 
    elif 'advisor' in text and 'resp' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='http://www.grad.uci.edu/academics/graduate%20advisor%20responsibilities/index.html')                 
    #elif 'wtf' in text: 
        #bot.send_message(chat_id=update.message.chat_id, text='WTF=> Where To my Friend!')
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
    elif 'hot' in text and 'you' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Oh thank you!, I am glad you find me hot, but please keep personal comment to yourself!')    
    elif 'what' in text and 'is' in text and 'this' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Well! I donot know what it is actually!')        
    elif 'preliminary' in text and 'exam' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='find more details here http://engineering.uci.edu/dept/eecs/graduate/roadmap_phd/prelim_cpe1')            
    elif 'pick' in text and 'me' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='I would but i donot have car! sorry') 
    elif 'spicy' in text and 'like' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Spicy food is the best food, although Haeseung cannot handle it!')       
    elif 'course' in text and 'quarter' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Get more details on courses https://www.reg.uci.edu/perl/WebSoc') 
    #elif 'yea' in text: 
        #bot.send_message(chat_id=update.message.chat_id, text='Heck Yeah!')
    elif 'hello' in text and 'wango' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Hi, how can i help you?')  
    #elif 'nice' in text: 
        #bot.send_message(chat_id=update.message.chat_id, text='Thank you!')
    elif 'too' in text and 'small' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='Is that why she is upset with you! there there!') 
    elif 'too' in text and 'big' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='That is what he or she said! #nogenderbias')     
    elif 'cold' in text and 'it' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='cold cold go away make some way for the sun!')
    elif 'annoy' in text and 'you' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='sorry, I know i can be annoying sometimes!') 
    #elif 'wow' in text: 
       # bot.send_message(chat_id=update.message.chat_id, text='wow! What did i miss?')   
    elif 'japan' in text: 
        bot.send_message(chat_id=update.message.chat_id, text='私の名前はジャンゴ・ワンゴです')  
    elif 'haha' in text or 'lol' in text: 
        bot.send_message(chat_id=update.message.chat_id, text=':)')    
    elif 'love' in text and 'you' in text: 
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
  


