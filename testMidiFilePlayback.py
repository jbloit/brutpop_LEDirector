from mido import MidiFile

mid = MidiFile('16notesAscending.mid')
for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        print(msg)