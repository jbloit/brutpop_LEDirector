import mido
print("TEST MIDI IN")

# Get list of available ports
mido.get_output_names()


lpd = mido.get_input_names()[0]
port = mido.open_input(lpd)

print(lpd)

for msg in port:
	print(msg)

