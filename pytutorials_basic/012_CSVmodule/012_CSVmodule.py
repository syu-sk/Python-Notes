import csv

#csv - comma-separated values. in long lists, it is unrealistic to manually retrieve information
#thus csv module is used to efficiently parse, read, write files


'''reading csv files'''
with open('csvsupport.csv', 'r') as csv_f:
	csv_reader = csv.reader(csv_f)	#.reader() - csv function. it is an iterable

	with open('csv_write.csv', 'w', newline='') as csv_w:
		#newline argument,so written data does not have extra line

		csv_writer = csv.writer(csv_w, delimiter = '\t')	 #.writer()
		#delimiter is the 'separator', notably default is comma
		#if the file contains characters == delimiter, inverted double commas are placed around the whole value
		
		for line in csv_reader:
			csv_writer.writerow(line)  
			#.writerow() edits the created file using the provided delimiter

			#print(line)
			#this returns lists containing each value, line by line
			#note indexes can be passed through these lists to isolate values


'''dictreader/writer'''
with open('csvsupport.csv', 'r') as csv_df:
	csv_reader = csv.DictReader(csv_df)
	#.DictReader() is an iterable which returns dictionaries with the top row being the keys, and subsequent rows after that the values.

	# for line in csv_reader:
	# 	print(line)
		#line is now a dictionary, [key] can be used

	with open('csv_dictwrite.csv', 'w', newline='') as csv_dw:

		fieldnames = ['Login email', 'Identifier', 'First name', 'Last name']

		csv_writer = csv.DictWriter(csv_dw, fieldnames=fieldnames, delimiter='\t')

		csv_writer.writeheader()

		for line in csv_reader:
			csv_writer.writerow(line)
		#del can be used to remove a key. though also remember to remove it from fieldnames

		#For DictWriter:
		#1. fieldnames required, these are the 'keys' from your dictionary
		#2. these fieldnames must be the same ones in the csv
		#3. include fieldnames argument in dictwriter function
		#4. .writeheader() to show fieldnames when writing