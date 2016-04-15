#!/usr/bin/python

# Modules

import sys
import os.path
import cgi

# Get information from the dashboard form

form = cgi.FieldStorage()

# Definitions

CURRENT = form.getvalue('username', 'No user')
BEGIN = "Content-type:text/html\n\n" + "<html lang=\"en\"><head><title>Add Friends</title><link rel=\"stylesheet\" type=\"text/css\" href=\"../css/main.css\"></head><body><center><font class=\"light-input\"size=\"5\"> Here are all the users on our system : </font> <br/><br/>"
END = "</body></html>"
ERROR_MSG = BEGIN + "Caramba !" + END
FORM_BEGIN = "<form class=\"light-input\" action=\"newfriends.py\" method=\"POST\" target=\"_self\">"
FORM_END = "<br/><input type=\"hidden\" name=\"username\" value=\"" + CURRENT + "\"><button type=\"submit\" class=\"bg-success\">ADD FRIENDS !</button></form></center>"
BACK_TO_DASHBOARD = "<form action=\"dashboard.py\" method =\"post\" target=\"_self\"><input type=\"hidden\" name=\"username\" value=\"" + CURRENT + "\"><button type=\"submit\"> GO BACK TO MY DASHBOARD </button></form>"

# Open users.txt to retrieve Usernames/Full names

UserList = []


if os.path.isfile('users.txt'):
    f = open("users.txt", "r")
else:
    sys.exit(ERROR_MSG)



for line in f:
    UserList.append(line.split(';'))

f.close()

# Generate a form with the previously recovered entries

print BEGIN
print FORM_BEGIN
for i in range(0, len(UserList)):
    if UserList[i][0]!= CURRENT:
        print "<input type=\"checkbox\" name=\"" + UserList[i][0] + "\" value=\"on\" /> <b>" + UserList[i][2] + "</b> (Username: <i><b>" + UserList[i][0] + "</b></i>)"
        print "<br/>"
print FORM_END
print BACK_TO_DASHBOARD
print END
