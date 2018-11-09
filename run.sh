#!/bin/bash

docker build -t indicium-telegram-bot .
docker run -d indicium-telegram-bot