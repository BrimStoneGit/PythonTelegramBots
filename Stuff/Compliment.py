import time
import telepot

def handle(msg):
    command = msg['text']
    content_type, chat_type, chat_id = telepot.glance(msg)
    
    if command == '/start':
        bot.sendMessage(chat_id, 'Willkommen zum deutschen Kompliment Bot :)\nSchreibe /compliment um ein Kompliment zu erhalten.')
    
    if command == '/compliment':
        bot.sendMessage(chat_id, 'Du siehst heute aber mal wieder gut aus ;)')
        
    if command == '/exit':
        exit()
        
    print 'ChatID: %s, Message: %s' % (chat_id, command)
    
bot = telepot.Bot('274416633:AAEVilV82hF_ppcBIqFfUsWWJ1e3Kzw8nMs')
bot.message_loop(handle)
print 'Ready to set of'

while 1:
    time.sleep(10)