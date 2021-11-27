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

"""
print (colored(banner, "red"))
print (colored(title, "yellow"))
print (colored(numbers,"cyan"))

inpt = input("Choose Number : ")
if inpt == "1":
	import siteInfo

if inpt == "2":
	import sourceCode
	
if inpt == "3":
	import subdomain
	
if inpt == "4":
	import paths

if inpt == "5":
	import dos

if inpt == "6":
	import dnsSniff

if inpt == "7":
	import portScanner
	
if inpt == "8":
	import scanM
	
else:
	inpt = input("Choose Number : ")
