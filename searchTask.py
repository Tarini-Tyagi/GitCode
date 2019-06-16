#!/usr/bin/python3
import time
import pyqrcode
from pyqrcode import QRCode
from googlesearch import search
web = input("Enter your query : ")
#print(search(web))
url=[]
count=0
for i in search(web,stop=3):
	# generating qr code
	surl = pyqrcode.create(i)
	# create and save the png
	count+=1 
	name = "myqr"+str(count)+".png"
	print(name)
	surl.svg(name, scale=8)
	url.append(i)
print("URL are : ")
print(url)
