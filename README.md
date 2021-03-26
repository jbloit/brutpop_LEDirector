# brutpop_LEDirector
RPI script(s) for running LED neopixel rings, controlled from midi.

## RaspberryPi Wiring

We do it [this way](https://learn.adafruit.com/neopixels-on-raspberry-pi/raspberry-pi-wiring#using-external-power-source-without-level-shifting-3005993-11)

## Installation from scratch

### OS installation
- Install [PatchBox OS](https://blokas.io/patchbox-os/) on a micro-sd card. Insert the card in the pi.
- plug a keyboard and screen to the pi and power it.
- On first launch, the login is "patch", the password is "blokaslabs"
- On first launch, the setup wizard should launch after login. You can change the password. I set it to "brutpop".
- set the boot environment to desktop, it will be a litte easier for setting up the pi. 

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







### Notes:

- list midi devices:
```bash
amidi -l
```


### Links:

- https://ixdlab.itu.dk/wp-content/uploads/sites/17/2017/10/Setting-Up-Raspberry-Pi-for-MIDI.pdf
- https://github.com/Hecsall/Raspberry-MIDI-Controller

