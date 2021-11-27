from banner import *
banner = port_scanner
print (colored(banner, "red"))

soc= socket.socket(socket.AF_INET)
ip = input("Enter Ip : ")
port = int(input("Enter Port : "))

def scan(port):
	if soc:
		try:
			soc.connect((ip,port))
		except:
			return False
		else:
			return True

if scan(port):
	print (colored(f"This Port {port} Is Open","red"))
else:
	print (colored(f"This Port {port} Is Close","green"))
	