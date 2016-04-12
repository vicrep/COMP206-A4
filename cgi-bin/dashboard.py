#!/usr/bin/python
import cgi, cgitb
import re
print("Content-Type: text/html")
print
print "<html>"
print "<body>"
username = "bob101"
print "<head><link rel=\"stylesheet\" type=\"text/css\" href=\"dashboard.css\"></head>"
print "<h2>Welcome to your Dashboard</h2>"

#menu logout, make a friend, and see a friend
print "<p>Menu</p>"
print "<div class=\"mymenu\">"
print "<ul>"
print " <li><a href=\"#\"> Logout </a>"
print " <li><a href=\"#\"> Make A Friend </a>"
print " <li><a href=\"#\"> See A Friend </a>"
print "</ul>"
print "</div>"

#status
print "<form name=\"input\" action=\"http://cgi.cs.mcgill.ca/~jpined1/status.py\" method=\"get\">"
print "  <b>Status: <input type=\"text\" name=\"status\"></br>"
print "  <input type=\"submit\" value=\"Submit\">"
print "</form>"

#20 most recent status updates
print "<h1>Newsfeed</h1>"
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
                if line.split(None,1)[0] in friendsList:
                        statusUpdate = line
                        friendName = line.split(' ',1)[0]
                        statusUpdate = line.split(' ',1)[1]
                        print "<p>"+ friendName + "</br></p>"
                        print "<p>" + statusUpdate
                        print
                        count += 1

print "</body>"
print "</html>"