#!/usr/bin/python
import os
import sys
import time
# Set color
G = '\033[32m' # Green
N = '\033[1;37m' # Netral
social = raw_input("Do you want to install? [y/n] : ")
if social == 'y' or social == 'y':
	os.system("clear")
	print " Wait downloading packages.."
	time.sleep(1)
	os.system("apt-get install perl")
	print "Done.."
	os.system("apt-get install Build-essential")
	print "Done.."
	os.system("apt-get install libany-uri-escape-perl")
	print "Done.."
	os.system("apt-get install libhtml-html5-entities-perl")
	print "Done.."
	os.system("apt-get install libhtml-entities-numbered-perl")
	print "Done.."
	os.system("apt-get install libhtml-parser-perl")
	print "Done.."
	os.system("apt-get install libwww-perl")
	print "Done.."
	print "Downloading requests module.."
	os.system("pip install requests")
	print "Done.."
	print "Downloading mechanize.."
	os.system("pip install mechanize")
	print "Done.."
	print
	print
	print ""+G+" Selesai xd sekarang tinggal ketik python social.py"+N+""
	raw_input("Press enter to exit..")
	os.system("clear")
	sys.exit()
