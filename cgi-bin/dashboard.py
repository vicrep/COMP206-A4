#!/usr/bin/python
import cgi, cgitb
import re

form = cgi.FieldStorage()
print("Content-Type: text/html")
print
print "<html>"
print "<head><link rel=\"stylesheet\" type=\"text/css\" href=\"..\css\main.css\"></head>"
print "<body>"
print "<div class=\"dashboard\">"
print "<h2>Welcome to your Dashboard</h2>"

#menu logout, make a friend, and see a friend
print "<div class=\"mymenu\">"
print "<ul>"
print " <li><a href=\"../\"> Logout </a>"
print " <li><a href=\"#\"> Make A Friend </a>"
print " <li><a href=\"#\"> See A Friend </a>"
print "</ul>"
print "</div>"

#status
print "<div class=\"statusUpdate\">"
print "<form name=\"input\" action=\"http://cgi.cs.mcgill.ca/~jpined1/cgi-bin/status.py\" method=\"get\">"
print "  <b>Status: <input type=\"text\" name=\"status\"></br>"
print "  <button type=\"submit\" class=\"bg-success\">Update</button>"
print "</form>"
print "</div>"

#20 most recent status updates
print "<h1>Newsfeed</h1>"
print "<div class=\"newsfeed\">"

with open("friends.txt") as friend:
        for line in friend:
                if line.split(None,1)[0] == 'bob11':
                        friends = line
friendsList = re.sub("[^\w] ", " ", friends).split()
statusFile = open("status.txt",'r')
lines = statusFile.readlines()
statusFile.close()
lines.reverse()
count = 0
for line in lines:
        if count < 20:
                #if line.split(None,1)[0] in friendsList:
                statusUpdate = line
                friendName = line.split(' ',1)[0]
                statusUpdate = line.split(' ',1)[1]
                print "<div class=\"post\">"
                print "<p><b>"+ friendName + "</b></br></p>"
                print "<p>" + statusUpdate
                print "</div>"
                count += 1

print "</div>"
print "</div>"
print "</body>"
print "</html>"
