import time 
import board 
import neopixel
import mido

## CONSTANTS
DATA_PIN = board.D18
NUM_STEPS = 16
NUM_RINGS = 8
ORDER = neopixel.RGB
BRIGHTNESS = 0.7
NUM_PIXELS = NUM_STEPS * NUM_RINGS

COLORS = [(255,0,0), (0,255,0), (0,0,255)]

## GLOBALS
strip = neopixel.NeoPixel (DATA_PIN, NUM_PIXELS, pixel_order=ORDER, brightness=BRIGHTNESS)
midiInput = mido.get_input_names()[0]




#
## RINGS
class Ring:
	def __init__(self, index, note, control):

		# the pixel ring index. Valid range = [ 0, NUM_RINGS - 1]
		self.index = index

		# the midi note triggering the ring. Valid range = [0, 127].
		self.note = note

		# the midi control number that the ring reacts to. Valid range = [0, 127]
		self.control = control

		# keep a reference to the first led index of the ring
		self.start = index * NUM_STEPS

		# keep a reference to the last led index of the ring
		self.end = index * NUM_STEPS + NUM_STEPS - 1

		# the brightness of the ring. Valid range = [0.0, 1.0]
		self.alpha = 1

		# is the ring On?
		self.isOn = False

		# the mode.
		# mode 0 : white light, either ON/OFF, cc changes brightness.
		# mode 1 : coloured light (3 colours), either ON/OFF, CC value changes colour.
		# mode 2 : patterns.

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
				if (ccVal < 42):
					self.color = 0
				elif (ccVal < 84):
					self.color = 1
				else:
					self.color = 2
				if (self.isOn):
					self.noteOn(self.note)

	def pc(self, progVal):
		if (progVal>2):
			progVal = 2
		if (progVal<0):
			progVal = 0
		self.mode = progVal


## Create the 8 ring objects
ring0 = Ring(0, 36, 1)
ring1 = Ring(1, 37, 2)
ring2 = Ring(2, 38, 3)
ring3 = Ring(3, 39, 4)
ring4 = Ring(4, 40, 5)
ring5 = Ring(5, 41, 6)
ring6 = Ring(6, 42, 7)
ring7 = Ring(7, 43, 8)

## MAIN
print('waiting for MIDI events from input : {}'.format(midiInput))

try:
	port = mido.open_input(midiInput)
except:
	print("could not open MIDI port")

for msg in port:
	if (msg.type=='note_on'):
		ring0.noteOn(msg.note)
		ring1.noteOn(msg.note)
		ring2.noteOn(msg.note)
		ring3.noteOn(msg.note)
		ring4.noteOn(msg.note)
		ring5.noteOn(msg.note)
		ring6.noteOn(msg.note)
		ring7.noteOn(msg.note)

	if (msg.type=='note_off'):
		ring0.noteOff(msg.note)
		ring1.noteOff(msg.note)
		ring2.noteOff(msg.note)
		ring3.noteOff(msg.note)
		ring4.noteOff(msg.note)
		ring5.noteOff(msg.note)
		ring6.noteOff(msg.note)
		ring7.noteOff(msg.note)


	if (msg.type=='control_change'):
		ring0.cc(msg.control, msg.value)
		ring1.cc(msg.control, msg.value)
		ring2.cc(msg.control, msg.value)
		ring3.cc(msg.control, msg.value)
		ring4.cc(msg.control, msg.value)
		ring5.cc(msg.control, msg.value)
		ring6.cc(msg.control, msg.value)
		ring7.cc(msg.control, msg.value)

	if (msg.type=='program_change'):
		ring0.pc(msg.program)
		ring1.pc(msg.program)
		ring2.pc(msg.program)
		ring3.pc(msg.program)
		ring4.pc(msg.program)
		ring5.pc(msg.program)
		ring6.pc(msg.program)
		ring7.pc(msg.program)
