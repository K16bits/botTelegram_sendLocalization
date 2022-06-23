import os

from telegram.ext import(
    Updater,
    CommandHandler,
    CallbackContext,
    MessageHandler,
    Filters
)

from database import Database
database = Database()

from dotenv import load_dotenv
load_dotenv(".env")
keyApi = os.environ.get("KEY_API")

def start(update:Updater,context:CallbackContext):
    # print(update)
    custom_keyboard = {
        "keyboard":[
            [{
            "text":"Enviar Localização",
            "request_location":True,
            }]
            ],
        "one_time_keyboard": True
        } 

    userID = update.message.chat.id
    context.bot.send_message(
        chat_id=userID,
        text="Envie sua localização:",
        reply_markup=custom_keyboard
    )

def getLocation(update,context:CallbackContext):
    location = update.message.location
    latitude  = location.latitude
    longitude  = location.longitude
    name = update.message['chat']['first_name']
    
    database.insertData(name,latitude,longitude)

    userID = update.message.chat.id
    context.bot.send_message(
        chat_id=userID,
        text="Localização enviado para o Banco de Dados"
    )


updater = Updater(token=keyApi)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("loc",start))
dispatcher.add_handler(MessageHandler(Filters.location, getLocation))

updater.start_polling()
updater.idle()