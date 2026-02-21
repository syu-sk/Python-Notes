import shutil

'''
shutil allows the unpacking/packing of the following formats:
- zip
- tar
- gztar: gzip'ed tar-file
- bztar: bzip2'ed tar-file
- xztar: xz'ed tar-file
'''


'''Making and Unpacking archives''' 
def example1():

	shutil.make_archive('zipfile2', 'zip', 'extractfile')
	#.make_archive(archive name, mode, file to make into archive)

	shutil.unpack_archive('zipfile2.zip', 'extractfile2')
	#.unpack_archive(archive name(with extension), directory name)

	#as above, shutil also allows making/unpacking gzip archives, which uses the same format as above, instead replacing zip with gztar

#example1()