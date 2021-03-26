from mido import MidiFile

mid = MidiFile('16notesAscending.mid')

for msg in mid.play():
    print(msg)

