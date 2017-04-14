'''
Created on 06.01.2017

@author: Benny
'''
# -*- coding: utf-8 -*-
import time
import telepot
from library import library

library = library()


def convertText(text):
#    wordDetected = False
#    newText = text
#    try:
#        for key, value in library.items():
#            newText = newText.replace(key, value)
#        if (text != newText):
#            wordDetected = True
#            return(newText.replace("ä", "ae").replace("ö", "oe").replace("ü", "ue"))
#        return(newText)
#    except:
#        if wordDetected:
#            return("Irgendwas in der Nachricht passt mir nicht.")
#        else :
#            return "Gönn dir"
    for key in library.wordMap:
        text = text.replace(key, library.wordMap[key])
    return text

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    chat_id = msg['chat']['id']
    message = msg['text']
    
    print (chat_id)
    
#    if message[0] == "/" :
        
    if content_type == 'text':
        if convertText(message) != message:
            bot.sendMessage(chat_id, convertText(message))
            print (convertText(message))
        else :
            print (message)
bot = telepot.Bot('307456324:AAFOHDqwu4VQFeUNfrwCzI7rxqfkxQqzCqs')
bot.message_loop(handle)
print ("Ready to set of")


while 1:
    time.sleep(10)
