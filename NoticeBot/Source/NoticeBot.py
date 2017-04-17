# -*- coding: utf-8 -*-
import time
import telepot
import telepot.namedtuple
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    chat_id = msg['chat']['id']
    if (content_type == 'text') :
        message = msg['text']
    else :
        bot.sendMessage(chat_id, 'Bitte Textnachricht eingeben')
        return
    
    
    print (chat_id)
    
    messageList = message.split(' ', 1)
    if messageList[0] == '/NewNotice' :
        myMessage = bot.sendMessage(chat_id, 'Deine Notiz lautet: ' + messageList[1])
        bot.sendMessage(chat_id, 'Soll ich diese Notiz aufnehmen?', 'Markdown', False, False, myMessage['message_id'], yesNoKeyboard)
    else :
        bot.sendMessage(chat_id, 'Ich weiß nicht, was du von mir willst...')
    
bot = telepot.Bot('225249137:AAH1X8cObiVtsJvtzOsgIdEtKCt7hX5llL0')    
yesButton = KeyboardButton()
yesButton['text'] = '/yes'
noButton = KeyboardButton()
noButton['text'] = '/no'
yesNoKeyboard = ReplyKeyboardMarkup()
yesNoKeyboard['keyboard'] = [[yesButton], [noButton]]
bot.message_loop(handle)
print ("Ready to set of")


while 1:
    time.sleep(10)
