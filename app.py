import telegram.ext
import time
import telegram
import os















zaman = time.strftime(" %d:%m:%Y %H:%M:%S")
with open('token.txt', 'r') as f:
    TOKEN = f.read()

def content1(update, bos):





def inp():
    
    input = update.message.text


def test(update, context):



    

   

  


    
    
    



def start(update, context):
    update.message.reply_text("Merhaba hoşgeldiniz")
    
  
    tests = open('hosgeldin.png', 'rb')
    time.sleep(3)

    update.message.reply_photo(tests)
    
    
    



    
def content(update, hakkinda):

#Gokhan Bey



def contact(update, context):
    update.message.reply_text("Yet")

updater = telegram.ext.Updater(TOKEN, use_context=True)
disp = updater.dispatcher


disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("test", test))
disp.add_handler(telegram.ext.CommandHandler("bos", content1))
disp.add_handler(telegram.ext.CommandHandler("hakkinda", content))

updater.start_polling()
updater.idle()


