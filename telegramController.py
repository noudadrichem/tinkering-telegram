import telegram
import schedule
from os import environ
from time import sleep
from calendarController import isThereANewEvent

TOKEN = environ.get('TOKEN')
bot = telegram.Bot(token=TOKEN)

chatId = bot.get_updates()[-1].message.chat_id

def onTheDay():
  print('Checking activities status')
  isNewEvent = isThereANewEvent()['isNewEvent']

  if isNewEvent:
    newActivityName = isThereANewEvent()['newEvent']['name']
    newActivityId = isThereANewEvent()['newEvent']['activityId']
    print('Er is een nieuwe activiteit geconstateerd met de naam {}'.format(newActivityName))


    text = '{}\n\nGa voor meer info naar https://indicium.hu/activiteiten/details/{}'.format(newActivityName, newActivityId)

    bot.send_message(
      chat_id=chatId,
      text=text
    )

  else:
    print('Geen nieuwe activiteit gevonden')


schedule.every(1).hour.do(onTheDay)

while True:
  schedule.run_pending()
  sleep(10)
