import sys
import time
import telepot

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        bot.sendMessage(chat_id, msg['text'])


#TOKEN = sys.argv[1]  # get token from command-line

bot = telepot.Bot('285778181:AAEeYgkdkHhPdKVic041GM1F3UM9jtBifT8')
bot.message_loop(handle)
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)