# brutpop_LEDirector
RPI script(s) for running LED neopixel rings, controlled from midi.

## RaspberryPi Wiring

We do it [this way](https://learn.adafruit.com/neopixels-on-raspberry-pi/raspberry-pi-wiring#using-external-power-source-without-level-shifting-3005993-11)
[This diagram](https://www.raspberrypi.org/documentation/usage/gpio/) of the GPIO pins of the pi can be useful.

## Installation from scratch

### OS installation



- Install [PatchBox OS](https://blokas.io/patchbox-os/) on a micro-sd card. Insert the card in the pi.
- plug a keyboard and screen to the pi and power it.
- On first launch, the login is "patch", the password is "blokaslabs"
- On first launch, the setup wizard should launch after login. You can change the password. I set it to "brutpop".
- set the boot environment to desktop, it will be a litte easier for setting up the pi. 
- For the following steps, you need an internet connection, make sure you connect to a wifi.

*NB* if you need to reconfigure, open a terminal and type 'patchbox'

### Install the required python3 libraries

First, install pip3, the package manager for python3.
In a terminal, type :
```bash
sudo apt update
sudo apt install python3-pip
```
Type 'y' when prompted.

The library to control neopixel LEDs from python 
```bash
sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel
sudo python3 -m pip install --force-reinstall adafruit-blinka
```

[see this link](https://learn.adafruit.com/neopixels-on-raspberry-pi/python-usage)


### Copy the sources
Download the code from this project, this will create a local folder called brutpop_LEDirector

```bash
cd
git clone https://github.com/jbloit/brutpop_LEDirector.git
```

## Run the code

open a terminal window and type
```bash
cd 
cd brutpop_LEDirector
sudo python3 main.py
```
It should reply with something like:
```bash
waiting for MIDI events from input : LPD8:LPD8 MIDI l 20:0
``` 

### autostart


### Shutdown button

button wired to GPIO pin 3 and ground.
added this line to /boot/config.txt :

```bash
dtoverlay=gpio-shutdown,gpio_pin=3
```




### Notes:

- list midi devices:
```bash
amidi -l
```


### Links:

- https://ixdlab.itu.dk/wp-content/uploads/sites/17/2017/10/Setting-Up-Raspberry-Pi-for-MIDI.pdf
- https://github.com/Hecsall/Raspberry-MIDI-Controller

