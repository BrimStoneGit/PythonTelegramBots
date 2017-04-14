# -*- coding: utf-8 -*-
import time

wordMap = {"idiot" : "alphakevin",
           "witz" : "eins nicer lustig",
           "cool" : "fly"}
 
def convertText(text):
    wordDetected = False
    newText = text
    try:
        for key, value in wordMap.items():
            newText = newText.replace(key, value)
        if (text != newText):
            wordDetected = True
            return(newText.replace("ä", "ae").replace("ö", "oe").replace("ü", "ue"))
        return(newText)
    except:
        if wordDetected:
			print 'Fehler'
            return 'Irgendwas in der Nachricht passt mir nicht.'
 
convertText("Geiler Text")
convertText("cooler Täxt")

while 1:
	time.sleep(10)