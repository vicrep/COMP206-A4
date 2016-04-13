#!/usr/bin/python

# Modules for CGI handling

import sys
import os.path
import cgi,cgitb

# Definitions

BEGIN = "Content-type:text/html\n\n" + "<html><head><link rel=\"stylesheet\" type=\"text/css\" href=\"../css/main.css\"></head><body>"
END = "</body></html>"
ERROR_MSG = BEGIN + "Caramba" + END
FORM_BEGIN = "<form action=\"/cgi-bin/newfriends.py\" method=\"POST\" target=\"_blank\">"
FORM_END = "<input type=\"submit\" value=\"Add Friends !\" /></form>"
BACK_TO_DASHBOARD = "<form action=\"dashboard.html\"><input type=\"submit\" value=\"Go back to my Dashboard\"></form>"
CURRENT = "currentusername"

# Retrieve Usernames/Full names

UserList = []

if os.path.isfile('../users.txt'):
    f = open("../users.txt", "r")
else:
    sys.exit(ERROR_MSG)

for line in f:
    UserList.append(line.split(';'))

f.close()

# Get MakeFriends form

form = cgi.FieldStorage()

# Get the list of selected users to befriend

FriendsList = []

for i in range(0, len(UserList)):
    if form.getvalue(UserList[i][0]):
        FriendsList.append(UserList[i][0])

# Add the selected users to the friends list of the current user in friends.txt

if os.path.isfile('../friends.txt'):
    f = open("../friends.txt", "r")
else:
    sys.exit(ERROR_MSG)

if os.path.isfile('../makefriends_buffer.txt'):
    buffer = open("../makefriends_buffer.txt", "w")
else:
    sys.exit(ERROR_MSG)

# -------------- Append Friends ------------------

NewFriends = ''
count = 0

for line in f:
    if line.split(None, 1)[0] == "currentusername":       # If this is the entry for the current user in friends.txt
         for i in range(0, len(FriendsList)):
            if FriendsList[i] not in line:      # If this is not already a friend
                NewFriends += FriendsList[i]
                count += 1
         if len(NewFriends)!=0:
                buffer.write(line.rstrip('\n') + " " + NewFriends + '\n')   # append new friends
         else:
                buffer.write(line)
    else:
         buffer.write(line)

# -----------------------------------------------

f.close()
buffer.close()

if os.path.isfile('../friends.txt'):
    f = open("../friends.txt", "w")
else:
    sys.exit(ERROR_MSG)

if os.path.isfile('../makefriends_buffer.txt'):
    buffer = open("../makefriends_buffer.txt", "r")
else:
    sys.exit(ERROR_MSG)

f.write(buffer.read())

buffer.close()
f.close()

# ---------------------------------------------

# Displaying the page

print BEGIN
if count>1:
        print str(count) + " friends have been added to your network !"
        print BACK_TO_DASHBOARD
        print END
elif count == 1:
    print "You've added a friend to your network !"
    print BACK_TO_DASHBOARD
    print END
else:
        print "These users were already your friends !"
        print BACK_TO_DASHBOARD
        print END

                                                                                                                                                                                                      108,0-1       Bot
