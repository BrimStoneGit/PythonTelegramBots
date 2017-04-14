import time
import telepot

def handle(msg):
    command = msg['text']
    
    if command == '/exit':
        exit()
        
    print 'Message: %s' % command
    
bot = telepot.Bot('285778181:AAEeYgkdkHhPdKVic041GM1F3UM9jtBifT8')
bot.message_loop(handle)
print 'Ready to set of'

while 1:
    time.sleep(10)