#!/usr/bin/python

import cgi, cgitb
import fileinput, os

form = cgi.FieldStorage()
CURRENT = form.getvalue('username', 'No User')
print("Content-Type: text/html")    # HTML is following
print
print "<html>"
print "<head><title>Status Update</title><link rel=\"stylesheet\" type=\"text/css\" href=\"../css/main.css\"></head>"

if form.getvalue('status'):
	line = form.getvalue('username') + ";" +form.getvalue('status')
	if os.stat("./status.txt").st_size == 0:
		with open("./status.txt","a") as f:
			f.write(line)
	else:
		# with open("./status.txt","a") as f:
		with open("./status.txt", 'r+') as f:
			content = f.read()
			f.seek(0, 0)
			f.write(line.rstrip('\r\n') + '\n' + content)
	print "<p>Status Updated"
else:
	print "<p>Status Empty"
print "<form action=\"dashboard.py\" method =\"post\" target=\"_self\"><input type=\"hidden\" name=\"username\" value=\"" + CURRENT + "\"><button type=\"submit\"> GO BACK TO MY DASHBOARD </button></form>"
print "</form>"
print "</html>"

