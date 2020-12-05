import mido
print("TEST MIDI IN")

# Get list of available ports
mido.get_output_names()


lpd = mido.get_input_names()[0]
port = mido.open_input(lpd)

print(lpd)

for msg in port:
	print(msg.dict())
	if(msg.type == 'note_on'):
		print('NOTE ON with note ')
		print(msg.note)

	if(msg.type == 'control_change'):
		print('CC with control ')
		print(msg.control)
		print('and value ')
		print(msg.value)

	
