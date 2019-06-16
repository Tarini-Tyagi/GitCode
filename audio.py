#!/usr/bin/python3
import pyttsx3
from datetime import datetime
import pip
import textwrap

def name(name):
	sound_driver=pyttsx3.init()
	sound_driver.say("hello "+name)
	sound_driver.runAndWait()

	now = datetime.now() 
	current_time = now.strftime("%H:%M:%S") 
	hrs=int(now.strftime("%H")) 
	min=int(now.strftime("%M")) 

	if hrs>4 and hrs<12: 
		print("Good Morning "+name) 
	elif hrs==12: 
		print("Good Afternoon " +name) 
	elif hrs>12 and hrs<15: 
		print("Good Afternoon " +name) 
	elif hrs>15 and hrs<22: 
		print("Good Evening " +name) 
	else: 
		print("You should sleep. It's "+current_time) 
		print("Have a good night")

def addnum(*x):
	
	print(sum(x))
	choice = input("Do you want to sort? Y/N : ")
	if choice=='Y':
		listsorted=sorted(x)
	print(listsorted)

def findnm():
	 installed_packages = pip.get_installed_distributions() 
	 installed_packages_list = sorted(["%s==%s" % (i.key, i.version) for i in installed_packages]) 
	 con=len(installed_packages_list)
	 print(con)
