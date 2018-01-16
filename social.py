#!\usr\bin\env python
# Social Engineering Attacks
# Coded by LOoL_Zec
# Instagram => @yungreyyxrist
# Plis dont change the rights pls :) The Hacker make tool not tool make a hacker ;)
import sys
import os
import time
# PUTIH TEBAL
N = '\033[1;37m'
# KUNING
O = '\033[1;33m'
# MERAH
R = '\033[1;31m'
# IJO
G = '\033[32m'
def restart_program():
   python = sys.executable
   os.execl(python, python, * sys.argv)
   curdir = os.getcwd()

if sys.platform == "linux2":
	os.system("clear")
elif sys.platform == "win32":
	os.system("cls")
else:
   python = sys.executable
   os.execl(python, python, * sys.argv)
   curdir = os.getcwd()

if sys.platform == "linux2":
	os.system("clear")
elif sys.platform == "win32":
	os.system("cls")
else:
	os.system("clear")
print
print
print ""+N+"              LOoLzeC Say"
print "        ------------------------"
print ""+N+"        <"+G+"   FUCK THE SOCIAL"+N+"    >"
print "        ------------------------"
print "       SOCIAL ENGINEERING ATTACKS"
print ""+G+"     -http://zumizec-com.waper.co-"+N+""
print
print
print " [1] "+O+"= >"+N+" FACEBOOK BRUTEFORCE"
print " [2]"+O+" = >"+N+" INSTAGRAM BRUTEFORCE"
print " [3]"+O+" = >"+N+" TWITTER BRUTEFORCE"
print " [4]"+O+" = >"+N+" HOTMAIL BRUTEFORCE"
print " [5]"+O+" = > "+N+"GMAIL BRUTEFORCE"
print ""+N+" [0]"+R+" Exit"+N+""
print
print
social = raw_input("Enter key bitch! > "+G+"")
if social == '01' or social == '1':
	os.system("clear")
	time.sleep(1)
	print ""+N+"          <"+G+" STARTING ATTACKS "+N+">"
	print
	print
	usr = raw_input("Enter Target = > : ")
	list = raw_input("Enter List = > : ")
	os.system("cd main;cd facebook;perl facebook.pl %s %s" % (usr,list))
	sys.exit()
elif social == '02' or social == '2':
	os.system("clear")
	time.sleep(1)
	print ""+N+"          < "+G+"STARTING ATTACKS"+N+" >"+N+""
	print
	print
	os.system("cd main;cd instagram;python2 instagram.py")
	sys.exit()
elif social == '03' or social == '3':
	os.system("clear")
	time.sleep(1)
	print ""+N+"          < "+G+"STARTING ATTACKS "+N+">"+N+""
	print
	os.system("cd main;cd twitter;python2 twitter.py")
	sys.exit()
elif social == '04' or social == '4':
	os.system("clear")
	time.sleep(1)
	print ""+N+"          < "+G+"STARTING ATTACKS "+N+">"
	print
	print
	usr = raw_input("Enter Email = > : ")
	list = raw_input("Enter List = > : ")
	os.system("cd main;cd hotmail;python2 hotmail.py -u %s -w %s" % (usr,list))
elif social == '05' or social == '5':
	time.sleep(1)
	os.system("clear")
	print ""+N+"         < "+G+" STARTING ATTACKS "+N+">"
	print
	print
	os.system("cd main;cd gmail;python2 gmail.py")
	sys.exit()
elif social == '0' or social == '00':
	print " Exiting.."
	time.sleep(2)
	print
	print ""+N+"   BYE :* "
	time.sleep(1)
	print
	sys.exit()
	
else:
	print ""+R+" Wrong Input KAMPANG 1!1!"
	time.sleep(1)
	print ""+G+"restaring..."+N+""
	time.sleep(2)
	restart_program()
