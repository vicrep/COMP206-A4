#!/usr/bin/python
import cgi, cgitb
import re

form = cgi.FieldStorage()
print("Content-Type: text/html")
print
print "<html>"
print "<head><link rel=\"stylesheet\" type=\"text/css\" href=\"../css/main.css\"></head>"
print "<body>"

CURRENT = form.getvalue('username', 'No user')

#menu logout, make a friend, and see a friend
print "<div class=\"mymenu\">"
print "<ul>"
print " <li><form action=\"../\" method =\"post\" target=\"_self\">"
print "  <input type=\"hidden\" name=\"username\" value=\"_\"></br>"
print "  <button type=\"submit\" class=\"bg-success\">LOGOUT</button>"
print "</form>"
print " <li><form action=\"./makefriends.py\" method =\"post\" target=\"_self\">"
print "  <input type=\"hidden\" name=\"username\" value=\""+ CURRENT +"\"></br>"
print "  <button type=\"submit\" class=\"bg-success\">MAKE A FRIEND</button>"
print "</form>"
print " <li><form action=\"./seefriends.cgi\" method =\"post\" target=\"_self\">"
print "  <input type=\"hidden\" name=\"username\" value=\""+ CURRENT + "\"></br>"
print "  <button type=\"submit\" class=\"bg-success\">SEE A FRIEND</button>"
print "</form>"
print "</ul>"
print "</div>"

print "<div class=\"dashboard\">"
print "<h2>Welcome to your Dashboard</h2>"
#status
print "<div class=\"statusUpdate\">"
print "<form name=\"input\" action=\"./status.py\" method=\"get\">"
print "  <b>Status: <input type=\"text\" name=\"status\"></br>"
print "  <input type=\"hidden\" name=\"username\" value=\"" + CURRENT + "\"></br>"
print "  <button type=\"submit\" class=\"bg-success\">Update</button>"
print "</form>"
print "</div>"

#20 most recent status updates
print "<h1>Newsfeed</h1>"
print "<div class=\"newsfeed\">"
friends=''
line=''
with open("friends.txt") as friend:
        for line in friend:
                if line.split(None,1)[0] == CURRENT:
                        friends = line
friends = line + CURRENT
friendsList = re.sub("[^\w] ", " ", friends).split()
statusFile = open("status.txt",'r')
lines = statusFile.readlines()
statusFile.close()
count = 0
for line in lines:
        if count < 20:
                if line.split(";",1)[0] in friendsList:
                	statusUpdate = line
                	friendName = line.split(";",1)[0]
                	statusUpdate = line.split(";",1)[1]
                	print "<div class=\"post\">"
                	print "<p><b>"+ friendName + "</b></br></p>"
                	print "<p>" + statusUpdate
                	print "</div>"
                	count += 1

print "</div>"
print "</div>"
print "</body>"
print "</html>"
