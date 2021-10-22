from banner import *
banner = data_sploit

title = "  [+] ------- Data Sploit ------- [+]"
numbers = """
1- Domain information
2- Download source code
3- Subdomain collector
4- Website paths collector
5- Dos attack
6- Dns spoofing
7- Port scanning
8- Port scanning manual
9- Get location
"""
print (colored(banner, "red"))
print (colored(title, "yellow"))
print (colored(numbers,"cyan"))

inpt = input("Choose Number : ")
if inpt == "1":
	import modules/siteInfo

if inpt == "2":
	import modules/sourceCode
	
if inpt == "3":
	import modules/subdomain
	
if inpt == "4":
	import modules/paths

if inpt == "5":
	import modules/dos

if inpt == "6":
	import modules/dnsSniff

if inpt == "7":
	import modules/portScanner
	
if inpt == "8":
	import modules/scanM

if inpt == "9":
	import ipAddrInfo
	
else:
	inpt = input("Choose Number : ")
