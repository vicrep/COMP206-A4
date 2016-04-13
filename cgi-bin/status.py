#!/usr/bin/python
import cgi, cgitb

form = cgi.FieldStorage()
usr = form.getvalue('username', 'No User')
print("Content-Type: text/html")    # HTML is following
print
print "<html>"
print "<head><title>Status Update</title><link rel=\"stylesheet\" type=\"text/css\" href=\"..\css\main.css\"></head>"

if form.getvalue('status'):
        with open("./status.txt","a") as myfile:
                line = form.getvalue('username') + ";" +form.getvalue('status')
                myfile.write(line+"\n")
        print "<p>Status Updated"
else:
        print "<p>Status Empty"
print "<form action=\"./dashboard.py\" method =\"post\" target=\"_blank\">"
print "  <input type=\"hidden\" name=\"username\" value=", usr,"></br>"
print "  <button type=\"submit\" class=\"bg-success\">Continue to Dashboard</button>"
print "</form>"
print "</html>"
