#!/usr/bin/python

# Modules

import sys
import os.path
import cgi

# Definitions

BEGIN = "Content-type:text/html\n\n" + "<html><head><link rel=\"stylesheet\" type=\"text/css\" href=\"../css/main.css\"></head><body>"
END = "</body></html>"
ERROR_MSG = BEGIN + "Caramba !" + END
FORM_BEGIN = "<form action=\"newfriends.py\" method=\"POST\" target=\"_blank\">"
FORM_END = "<input type=\"submit\" value=\"Add Friends !\" /></form>"
BACK_TO_DASHBOARD = "<form action=\"dashboard.html\"><input type=\"submit\" value=\"Go back to my Dashboard\"></form>"
CURRENT = 'currentusername'

# Open users.txt to retrieve Usernames/Full names

UserList = []


if os.path.isfile('../users.txt'):
    f = open("../users.txt", "r")
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
        print "<input type=\"checkbox\" name=\"" + UserList[i][0] + "\" value=\"on\" /> <b>" + UserList[i][2] + "</b> (Username: " + UserList[i][0] + ")"
        print "<br/>"
print FORM_END
print BACK_TO_DASHBOARD
print END
