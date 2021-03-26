import time
from mido import MidiFile

mid = MidiFile('16notesAscending.mid');

slowDownFactor = 1;

print ("this file is this long: ");
print (mid.length);

while True:
	for msg in mid:
    		time.sleep(msg.time * slowDownFactor)
    		print(msg)