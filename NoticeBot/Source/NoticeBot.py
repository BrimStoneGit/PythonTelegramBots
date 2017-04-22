# -*- coding: utf-8 -*-
import time
import telepot
import telepot.namedtuple
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
from builtins import str, int

def handle(msg):
    global yesNoKeyboard
    global myNotice
    global sureToSave
    global sureToDelete
    global lineToDelete
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
            file = open(str(chat_id) + '.txt', 'a+')
            file.write(myNotice + '\n')
            file.close()
            myNotice = ''
            sureToSave = False
        else :
            bot.sendMessage(chat_id, 'Notiz verworfen')
            myNotice = ''
            sureToSave = False
    elif sureToDelete :
        if message == '/yes' :
            bot.sendMessage(chat_id, 'Notiz gelöscht')
            file = open(str(chat_id) + '.txt', 'r')
            noticeArray = file.readlines()
            file.close()
            file = open(str(chat_id) + '.txt', 'w')
            for i in range(len(noticeArray)) :
                if i != lineToDelete :
                    file.write(noticeArray[i])
            file.close()
            sureToDelete = False
        else :
            bot.sendMessage(chat_id, 'Notiz nicht gelöscht')
            sureToDelete = False
    else :
        messageList = message.split(' ', 1)
        if messageList[0] == '/newNotice' :
            if len(messageList) == 2 :
                myNotice = messageList[1]
                myMessage = bot.sendMessage(chat_id, 'Deine Notiz lautet: ' + myNotice)
                sureToSave = True
                bot.sendMessage(chat_id, 'Soll ich diese Notiz aufnehmen?', 'Markdown', False, False, myMessage['message_id'], yesNoKeyboard)
            else :
                bot.sendMessage(chat_id, 'Bitte "/NewNotice Notiz" eingeben.')
        elif messageList[0] == '/showAll' :
            n = 'Deine Notizen sind: \n'
            file = open(str(chat_id) + '.txt', 'r+')
            noticeArray = file.readlines()
            i = 1
            for x in noticeArray :
                n += str(i) + ': ' + str(x)
                i += 1
            bot.sendMessage(chat_id, n)
            file.close()
        elif messageList[0] == '/deleteLine' :
            lineNr = messageList[1].split(' ', 1)
            delLine = int(lineNr[0])
            file = open(str(chat_id) + '.txt', 'r+')
            noticeArray = file.readlines()
            if len(noticeArray) < delLine :
                bot.sendMessage(chat_id, 'Du hast nur ' + str(len(noticeArray)) + ' Notizen. Ich kann Zeile ' + str(delLine) + ' nicht löschen.')
            else :
                lineToDelete = delLine - 1
                sureToDelete = True
                toBeDeleted = noticeArray[delLine - 1].replace("\n", "")
                bot.sendMessage(chat_id, 'Willst du "' + toBeDeleted + '" (Notiz Nr. ' + str(delLine) + ') wirklich löschen?')
        else :
            bot.sendMessage(chat_id, 'Entschuldigung, ich weiß nicht, was du von mir willst...')
    
bot = telepot.Bot('225249137:AAH1X8cObiVtsJvtzOsgIdEtKCt7hX5llL0')   

#global Values
global sureToSave
sureToSave = False 
global sureToDelete
sureToDelete = False
global myNotice 
global yesNoKeyboard 
global lineToDelete
yesNoKeyboard = ReplyKeyboardMarkup(keyboard = [[KeyboardButton(text = '/yes')], [KeyboardButton(text = '/no')]], one_time_keyboard = True)

bot.message_loop(handle)
print ("Ready to set of")


while 1:
    time.sleep(10)
