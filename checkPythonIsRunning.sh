#!/bin/bash

while [ true ]; do 
  if pgrep -x "python3" > /dev/null
  then
      echo "Running"
  else
      echo "Stopped"
      sudo /usr/bin/python3 /home/patch/brutpop_LEDirector/main.py
  fi
  sleep 5
done
