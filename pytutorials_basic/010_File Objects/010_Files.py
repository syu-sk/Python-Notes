#File objects


'''Reading Files'''

with open('files_support.txt', 'r') as file:
	# open function -- open('filename', 'mode'). mode can be r(read), w(write), a(append) as well as more advanced forms.
	# default mode is read
	# with is a context manager. i.e it opens the file, and closes it immediately when the code runs out of the block
	# if with is not used, file.close() needs to be put at the end of the code

	print(file.name)

	#.name returns the name of the file 
	#.mode returns mode
	#.closed returns boolean on whether file is closed

	# file_contents = file.read()  #() specifies number of characters to read. subsequent .read() will continue from when it last stopped
	# print(file_contents)

	#.readlines() instead forms a list with the lines in the file
	#.readline reads the first line of the file
	#.tell() returns the position, i.e where the last read() stopped
	#.seek() sets position. for example, if 0, the code starts reading from the start again

	for line in file:
		print(line, end='')

	#the above is a more efficient way to read, as opposed to .read which reads the whole file at once
	#end='' has to be present as by default, print enters to the next line upon ending, creating an extra line


'''Writing Files'''

with open('testfile.txt', 'w') as f:
	x = 1
	for i in range(50):
		f.write(f'{x}')
		x+=1
#write mode: if file exists, overwrite it with location at 0. if file doesnt, create a new file
#be careful of writing on existing files since it will overwrite. use append 'a' instead
#unable to read while in write mode. all other methods work

#to read/write images, the modes 'rb' and 'wb' have to be used. bytes instead of texts are read instead
#while in byte mode, simply read/write the image as per normal