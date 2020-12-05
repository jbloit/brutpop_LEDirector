import time 
import board 
import neopixel
import mido

## CONSTANTS
DATA_PIN = board.D18
NUM_STEPS = 16
NUM_RINGS = 2
ORDER = neopixel.RGB
BRIGHTNESS = 0.7
NUM_PIXELS = NUM_STEPS * NUM_RINGS

## GLOBALS
strip = neopixel.NeoPixel (DATA_PIN, NUM_PIXELS, pixel_order=ORDER, brightness=BRIGHTNESS)
midiInput = mido.get_input_names()[0]

## MAIN
print('waiting for MIDI events from input : {}'.format(midiInput))

alpha = 1;
port = mido.open_input(midiInput)
for msg in port:
	if (msg.type=='note_on'):
		strip[0] = (int(alpha*255),int(alpha*255),int(alpha*255))
	if (msg.type=='note_off'):
		strip[0] = (0,0,0)
	if (msg.type=='control_change'):
		alpha = msg.value/127
		print('alpha: {}'.format(alpha))

