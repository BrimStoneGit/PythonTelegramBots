# -*- coding: utf-8 -*-
import time
import telepot
import telepot.namedtuple
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton

def handle(msg):
    global yesNoKeyboard
    global myNotice
    global sureToSave
    content_type, chat_type, chat_id = telepot.glance(msg)
    chat_id = msg['chat']['id']
    if (content_type == 'text') :
        message = msg['text']
    else :
        bot.sendMessage(chat_id, 'Bitte Textnachricht eingeben')
        return
    
    
    print (chat_id)
    
    if sureToSave :
        if message == '/yes' :
            bot.sendMessage(chat_id, 'Notiz hinzugefügt')
            f = open(str(chat_id) + '.txt', 'a+')
            f.write(myNotice + '\n')
            f.close()
            myNotice = ''
            sureToSave = False
        else :
            bot.sendMessage(chat_id, 'Notiz verworfen')
            myNotice = ''
            sureToSave = False
    else :
        messageList = message.split(' ', 1)
        if messageList[0] == '/NewNotice' :
            myNotice = messageList[1]
            myMessage = bot.sendMessage(chat_id, 'Deine Notiz lautet: ' + myNotice)
            sureToSave = True
            bot.sendMessage(chat_id, 'Soll ich diese Notiz aufnehmen?', 'Markdown', False, False, myMessage['message_id'], yesNoKeyboard)
        elif messageList[0] == '/ShowAll' :
            n = 'Deine Notizen sind: \n'
            f = open(str(chat_id) + '.txt', 'r+')
            fl = f.readlines()
            i = 1
            for x in fl :
                n += str(i) + ': ' + str(x)
                i += 1
            bot.sendMessage(chat_id, n)
            f.close()
            
        else :
            bot.sendMessage(chat_id, 'Entschuldigung, ich weiß nicht, was du von mir willst...')
    
bot = telepot.Bot('225249137:AAH1X8cObiVtsJvtzOsgIdEtKCt7hX5llL0')   

global sureToSave
sureToSave = False 
#global yesSure = False
global myNotice 
#yesButton = KeyboardButton()
#yesButton['text'] = '/yes'
#noButton = KeyboardButton()
#noButton['text'] = '/no'
global yesNoKeyboard 
yesNoKeyboard = ReplyKeyboardMarkup(keyboard = [[KeyboardButton(text = '/yes')], [KeyboardButton(text = '/no')]], one_time_keyboard = True)
#yesNoKeyboard['keyboard'] = [[KeyboardButton(text = '/yes')], [KeyboardButton(text = '/no')]]
bot.message_loop(handle)
print ("Ready to set of")


while 1:
    time.sleep(10)
