#!/usr/bin/python
import cgi, cgitb

form = cgi.FieldStorage()

print("Content-Type: text/html")    # HTML is following
print
print "<html>"
print "<head><title>Status Update</title><link rel=\"stylesheet\" type=\"text/css\" href=\"..\css\main.css\"></head>"

if form.getvalue('status'):
        with open("./status.txt","a") as myfile:
                line = "username " + form.getvalue('status')
                myfile.write(line+"\n")
        print "<p>Status Updated"
else:
        print "<p>Status Empty"
print "</html>"
