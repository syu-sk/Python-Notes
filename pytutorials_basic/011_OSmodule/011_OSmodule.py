import os


'''Basic OS methods'''
print(os.getcwd())
#cwd - current working directory

os.chdir('C:/Users/User/OneDrive/python scripts/cstutorials/011_OSmodule')
#chdir - change directory. here the directory is changed to the same one
#in a directory, all components should be folders

print(os.listdir())
#listdir - lists all files/folders under that directory.

#os.path.join(path, tojoin) can be used to join a path and a directory to form a new desired path
#os.path.split(path) splits into directory and basename
#os.path.exists(path) returns boolean on whether the path exists
#os.path.isdir and os.path.isfile. self explanatory
#os.path.splitext(path) returns the path with the extension separated


'''Making and Removing directories'''

os.mkdir('mkdir')
os.makedirs('makedirs/innerfolder')

#mkdir can only create a singular folder
#makedirs can create a folder with subdirectories under it (innerfolder)
#just use makedirs all the time

os.rmdir('mkdir')
os.removedirs('makedirs/innerfolder')
print(os.listdir())
#likewise for rmdir and removedirs. however need to be careful when using removedirs
#careful for erasing 

#print(os.stat('ostest.txt'))
#os.stat returns certain attributes of the file given


'''os.walk'''
#os.walk is an iterable.

# for dirpath, dirnames, filenames in os.walk('C:/Users/User/OneDrive/python scripts'):
# 	print('Current Path: ', dirpath)
# 	print('Directories: ', dirnames)
# 	print('Files: ', filenames)
# 	print()

#loops through every folder in the given directory
#iterable has 3 components - the directory it is observing, and the folders and files in it
#note that when it observes a directory, it goes through everything in that directory before exiting


'''locating a file/directory'''
print(os.getenv('Public'))