import requests 
from os import environ

online = environ.get('ONLINE')
url = 'indicium.hu' if online else 'localhost:55242'  
getUrl = 'http://{}/api/v1/activities'.format(url)
fileToWrite = './eventsAmount.txt'

def writeNewNumberToFile(length):
  with open(fileToWrite, 'w') as file:
    file.write('{}'.format(length))

def isThereANewEvent():
  allCalendarEvents = requests.get(getUrl).json()
  currentCalendarEventAmount = len(allCalendarEvents)
  isNewEvent = False

  with open (fileToWrite, 'r') as file:
    fileLines = file.readlines()

    if len(fileLines) > 0:
      for lijn in fileLines:
        if currentCalendarEventAmount == int(lijn):
          isNewEvent = False
        else:
          isNewEvent = True
          writeNewNumberToFile(currentCalendarEventAmount)
    else:
      isNewEvent = True
      writeNewNumberToFile(currentCalendarEventAmount)

  return {
    'isNewEvent': isNewEvent, 
    'newEvent': allCalendarEvents[currentCalendarEventAmount-1]
  }
