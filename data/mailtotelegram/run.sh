#!/bin/bash

cd /opt/mailtotelegram

while true
do
./mailtotelegram.py 2>&1 > /dev/null
sleep 5
done
