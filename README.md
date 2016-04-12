# COMP206-A4
Final Assignment for COMP 206 - Intro to Software Systems (McGill, W'16)

## I. Setting up the hosting Server

Website will have :

1. Welcome/landing Pages
2. Login/new user profile page
3. Dashboard
4. View a friend's profile page
5. Make a friend page


## II. Creating the Website Pages

* Common Style/theme among all the Pages
* Choose color/Style
* Templates/authoring tools = badly
* Only HTML, CGI, C, Bash and Python. CSS/JavaScript allowed.

### The Welcome/Landing Pages

* Must display the website name in big letters
* At the bottom write : `created by + Team name.`
* Paragraph describing and promoting website to new users
* Simple menu directing people to either login/create account
* Directed towards a particular industry
* ONLY HTML

HTML + CGI + C

[GLORY=CSS]

### The Dashboard Pages
Python + HTML + CGI

### The Make a Friend Page
(Python)

+ Displays a **list of checkboxes with all the users** (*i.e* every user on users.txt) **except for the current user**

+ Once the "Add friends" button is clicked, display a message according to the number of new friends (if any) and allows the user to go back to the Dashboard

+ The new friends are appended at the current user's entry in friends.txt, **without repetition**.

+ Creates makefriends_buffer.txt (that gets erased and created again everytime we call the script) since I haven't figured out how to change a file in place in python...

### The See a Friend Page
C
