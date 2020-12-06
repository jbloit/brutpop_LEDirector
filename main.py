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

COLORS = [(230,20,100), (30,200,10), (0,20,100), (100,100,0)]



## GLOBALS
strip = neopixel.NeoPixel (DATA_PIN, NUM_PIXELS, pixel_order=ORDER, brightness=BRIGHTNESS)
midiInput = mido.get_input_names()[0]
#
## RINGS
class Ring:
	def __init__(self, index, note, control):
		self.index = index
		self.note = note
		self.control = control
		self.start = index * NUM_STEPS
		self.end = index * NUM_STEPS + NUM_STEPS - 1
		self.alpha = 1
		self.isOn = False
		self.mode = 0
		
		# for mode 1, current selected color index in COLORS array
		self.color = 0
		
		print('RING {} CTOR : range({}-{})'.format(index, self.start, self.end))

	def noteOn(self, pitch):
		if (pitch==self.note):
			if (self.mode == 0):
				self.isOn = True
				strip[self.start:self.end+1] = [(int(self.alpha*255),int(self.alpha*255),int(self.alpha*255))] * NUM_STEPS

			elif(self.mode == 1):
				self.isOn = True
				strip[self.start:self.end+1] = [COLORS[self.color]] * NUM_STEPS

			elif(self.mode == 2):
				self.isOn = True
				strip[self.start:self.end+1] = [(100,30,200)] * NUM_STEPS

	def noteOff(self, pitch):
		if (pitch==self.note):
			self.isOn = False
			strip[self.start:self.end+1] = [(0, 0, 0)] * NUM_STEPS

	def cc(self, ccNum, ccVal):
		if (ccNum==self.control):

			if (self.mode == 0):
				self.alpha = ccVal/127
				if (self.isOn):
					self.noteOn(self.note)

			elif (self.mode == 1):
				if (ccVal < 30):
					self.color = 0
				elif (ccVal < 60):
					self.color = 1
				elif (ccVal < 90):
					self.color = 2
				else:
					self.color = 3



	def pc(self, progVal):
		if (progVal>2):
			progVal = 2
		if (progVal<0):
			progVal = 0
		self.mode = progVal


ring0 = Ring(0, 36, 1)
ring1 = Ring(1, 37, 2)

## MAIN
print('waiting for MIDI events from input : {}'.format(midiInput))

port = mido.open_input(midiInput)
for msg in port:
	if (msg.type=='note_on'):
		ring0.noteOn(msg.note)
		ring1.noteOn(msg.note)

	if (msg.type=='note_off'):
                ring0.noteOff(msg.note)
                ring1.noteOff(msg.note)

	if (msg.type=='control_change'):
		ring0.cc(msg.control, msg.value)
		ring1.cc(msg.control, msg.value)

	if (msg.type=='program_change'):
		ring0.pc(msg.program)
		ring1.pc(msg.program)

