from subprocess import Popen, PIPE
import urllib.request

def check_installation(package):
	stdin =["which",package]
	p1 = Popen(stdin, stdout=PIPE)
	stdout, stderr = p1.communicate()

	if stderr!=None:
		print(stderr)
	elif stdout:
		print(stdout.decode('utf-8'))
		return False
	else:
		return True

def check_internetconnection():
	try:
	    urllib.request.urlopen('http://www.google.com')
	    return True
	except urllib.error.URLError:
	    return False
	except:
	    print("Memory limit exceeded")

def install_package(package):
	stdin =["sudo","apt-get","install", "-y" , package]
	p1 = Popen(stdin, stdout=PIPE)
	stdout, stderr = p1.communicate()

	if stderr!=None:
		print(stderr)
	else:
		print(stdout.decode('utf-8'))

def install_python_package(package):
		stdin =["sudo","-H","pip3", "install" , package]
		p1 = Popen(stdin, stdout=PIPE)
		stdout, stderr = p1.communicate()

		if stderr!=None:
			print(stderr)
		else:
			print(stdout.decode('utf-8'))

def start():
	packages = ["xsel", "python3-tk"]
	for package in packages:
		if check_installation(package):
			if check_internetconnection():
				print("installing", package,"...")
				install_package(package)
				print(package, "installed succesfully.")
			else:
				print("Please check Internet Connection!!!")
				break
		else:
			print("xsel","already found!!!")
	install_python_package("xlib>=0.17")
	install_python_package("pynput")

if __name__ == '__main__':
	start()
