from subprocess import Popen, PIPE
import urllib.request

def check_installation():
	stdin =["which","xsel"]
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

def install_package():
	stdin =["sudo","apt-get","install","xsel"]
	p1 = Popen(stdin, stdout=PIPE)
	stdout, stderr = p1.communicate()

	if stderr!=None:
		print(stderr)
	else:
		print(stdout.decode('utf-8'))

def start():
	if check_installation():
		if check_internetconnection():
			install_package()
		else:
			print("Please check Internet Connection!!!")
	else:
		print("xsel","already found!!!")

if __name__ == '__main__':
	start()
