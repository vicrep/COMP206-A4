#include <stdlib.h>
#include <string.h>
#include <stdio.h>

#include "users.h"


void getFriends(char *usr) {
    FILE *f = fopen(FRIEND_DATA, "r");
    int i = 0, j;
    char fBuf[512];
    char *friends[256];

    while(fgets(fBuf, 512, f) != NULL) {
        if(!strcmp(usr, strtok(fBuf, " "))) {
            friends[0] = strtok(NULL, " ");
            while(friends[i] != NULL) friends[++i] = strtok(NULL, " ");
        }
    }

    printf("<h2>My Friends:</h2>\n");
    if(i) {
        for (j = 0; j < i; j++) {
            printf("<button type='submit' form='seefriends' name='friend' value='%s'>%s</button>\n", friends[j], friends[j]);
        }
        printf("<button type='submit' form='seefriends' formaction='./dashboard.py'>Back to Dashboard</button>\n");
    } else {
        printf("<p><i>You don't have any friends yet!></i></p>\n");
        printf("<button type='submit' form='seefriends' formaction='./makefriends.py'>Add More Friends</button>\n");
    }
}

int main(void) {
    char c;
    int i = 0;
    char buffer[512];
    int len = atoi(getenv("CONTENT_LENGTH"));
    char *delim = "=&", *usr;

        while ((c = getchar()) != EOF && i < len) {
            if (i < 512) {
                if (c!='+') buffer[i] = c;
                else buffer[i]=' ';
                i++;
            }
        }

    buffer[i] = '\0';

    strtok(buffer, delim);
    usr = strtok(NULL, delim);

    RESP_HTML_START;
    printf("<form id='seefriends' method='post' action='./friend.cgi'><input type='hidden' name='username' value='%s'></form>", usr);
    if(usr == NULL) printf("<h2>Error</h2>\n<p>You don't have access to this page, please <a href='../login.html'>login</a> and try again!</p>\n");
    else getFriends(usr);
    RESP_HTML_END;

    exit(0);
}