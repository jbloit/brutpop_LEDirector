#!/bin/bash

while [ true ]; do 
  if pgrep -x "python3" > /dev/null
  then
      echo "Running"
  else
      echo "Stopped"
      python3 main.py
  fi
  sleep 5
done
