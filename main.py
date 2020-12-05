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

## RINGS
class Ring:
	def __init__(self, index, note, control):
		self.index = index
		self.note = note
		self.control = control
		self.start = index * NUM_STEPS
		self.end = index * NUM_STEPS + NUM_STEPS - 1
		self.alpha = 1
		print('RING {} CTOR : range({}-{})'.format(index, self.start, self.end))

	def noteOn(self, pitch):
		print('ON.PITCH IN {}, internal note {}'.format(pitch, self.note))
		if (pitch==self.note):
			for i in range (self.start, self.end+1):
				strip[i]= (int(self.alpha*255),int(self.alpha*255),int(self.alpha*255))
	def noteOff(self, pitch):
		print('OFF.PITCH IN {}, internal note {}'.format(pitch, self.note))
		if (pitch==self.note):
			for i in range (self.start, self.end+1):
				strip[i]= (0, 0, 0)
	def cc(self, ccNum, ccVal):
		if (ccNum==self.control):
			self.alpha = ccVal/127

ring0 = Ring(0, 36, 1)
ring1 = Ring(1, 37, 2)

## MAIN
print('waiting for MIDI events from input : {}'.format(midiInput))

port = mido.open_input(midiInput)
for msg in port:
	if (msg.type=='note_on'):
		print(msg.note)
		ring0.noteOn(msg.note)
		ring1.noteOn(msg.note)

	if (msg.type=='note_off'):
                ring0.noteOff(msg.note)
                ring1.noteOff(msg.note)

	if (msg.type=='control_change'):
		ring0.cc(msg.control, msg.value)
		ring1.cc(msg.control, msg.value)
