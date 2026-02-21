import subprocess


'''subprocess commands'''
def example1():

	p1 = subprocess.run('pip list', shell=True)
	#for windows, dir command is built into the shell, hence needing this extra shell argument
	#shell is from the device itself, only use when input is done personally by the user
	print(p1)
	#notice completed process is returned, assigning the variable does not allow remote running of the subprocess

	print(p1.args)
	#returns any arguments passed

	print(p1.returncode)
	#returns the returncode. 0 = nothing wrong

#example1()


'''stdout'''
def example2():

	p1 = subprocess.run('pip list', shell=True, capture_output=True, text=True)
	
	print(p1.stdout)
	#stdout (standard output) is the output from the shell. however, the output from the subprocess is simply a display on the console. the capture_output argument makes it such that this shell output is captured in the variable without running the command, allowing stdout return the output in byte format. this is then converted to text format via the text argument.
	#capture_output redirects stdout and stderr to the subprocess PIPE - stdout=subprocess.PIPE. essentially, output is 'frozen' in an intermediate stage which is retrieved manually (alternatively, stderr or returncode)

	with open('output.txt', 'w') as f:

		p1 = subprocess.run('pip list', shell=True, stdout=f, text = True)
		#it is also possible to redirect stdout to a file

#example2()


'''Error management'''
def example3():

		p1 = subprocess.run('pip list', shell=True, capture_output=True, text=True, check=True)
		print(p1)
		#the check argument returns a traceback error if the subprocess does not give returncode of 0

		p2 = subprocess.run('pip list -baddir', shell=True, stderr=subprocess.DEVNULL, text=True)
		print(p2)
		#redirecting the error into subprocess.DEVNULL neglects it, allowing the program to continue running even with an error, while still giving a returncode

example3()


