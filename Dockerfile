FROM python:3.6

COPY calendarController.py ./
COPY telegramController.py ./
COPY eventsAmount.txt ./
COPY requirements.txt ./

RUN pip install -r requirements.txt

ENV TOKEN= \
    ONLINE=True

CMD ["python", "telegramController.py"]