# Tinkering with Telegram

> Runs telegramController.py every hour in a daemonized docker container

### MacOS / Linux
```bash
sh run.sh
```

### Windows
```
# step 1
docker build -t indicium-telegram-bot .

#step 2
docker run -d indicium-telegram-bot
```