import zipfile
import os

'''Creating a Zip File Archive'''
def example1():

	with zipfile.ZipFile('zipfiles.zip', 'w', compression=zipfile.ZIP_DEFLATED) as my_zip:
	#.ZipFile(Archive name, mode) write mode since zip file is being created. compression is an optional argument to compress the files (so they take up lesser space), which by default is disabled.
		
		#my_zip is the variable the zip archive is assigned to
		my_zip.write('testfile.txt')
		my_zip.write('sample.jpeg')
		#similar to writing to a file, but the context manager enables writing entire files into the zipfile

#example1()


'''Accessing i.e reading the archive'''
def example2():

	with zipfile.ZipFile('zipfiles.zip', 'r') as my_zip:

		print(f'extracting: {my_zip.namelist()}') #list of zipped files
		my_zip.extractall('extractfile')
		#.extractall(directory). creates a directory where the extracted files are deposited
		#alternatively, .extract('file.ext') will extract a single selected file, though this extracts the file into the current working directory, instead of creating a directory for it

		print(f'successfully extracted: {os.listdir('extractfile')}')

#example2()