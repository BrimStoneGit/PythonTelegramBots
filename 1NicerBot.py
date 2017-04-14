# -*- coding: utf-8 -*-
import time
import telepot

wordMap = {"idiot" : "alphakevin",
			"cool" : "fly",
			"freundin" : "bae",
			"ist so" : "isso",
			"Bier" : "Hopfensmoothie",
			"chille" : "hartze",
			"witzig" : "1 nicer lustig",
			"chillen" : "hartzen",
			"chill" : "hartz",
			"gut" : "gg",
			"Ist das normal" : "IiiiiiiIiIIIiiIIIIiiiIIist das normal?",
			"Boss" : "Babo",
			"berühmt" : "fame",
			"schlecht" : "bg",
			"viel Spass" : "gönn dir",
            "Viel Spass" : "Gönn dir",}


def convertText(text):
    wordDetected = False
    newText = text
#    try:
#    for key, value in wordMap.items():
#        newText = newText.replace(key, value)
#        if (text != newText):
#            wordDetected = True
#            return(newText.replace("ä", "ae").replace("ö", "oe").replace("ü", "ue"))
#        return(newText)
#    except:
#        if wordDetected:
#           return("Irgendwas in der Nachricht passt mir nicht.")
#        else :
#            return "Gönn dir"
    for key, value in wordMap.items():
        text = text.replace(key, value)
    return text

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    chat_id = msg['chat']['id']
    message = msg['text']
    
    print (chat_id)
    
    if content_type == 'text':
        if convertText(message) != message:
            bot.sendMessage(chat_id, convertText(message))
            print (convertText(message))
        else :
            print ('No need to send something')
bot = telepot.Bot('285778181:AAEeYgkdkHhPdKVic041GM1F3UM9jtBifT8')
bot.message_loop(handle)
print ("Ready to set of")
#print(convertText("Du idiot, der witz war echt cool."))
#print(convertText("Geiler Täxt"))

while 1:
    time.sleep(10)
