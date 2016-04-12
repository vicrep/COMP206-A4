#include <stdlib.h>
#include <string.h>
#include <stdio.h>

#include "users.h"

BOOL isAuth(char* usr, char* pwd) {
    BOOL auth = FALSE;
    FILE *f = fopen(USR_DATA, "r");

    char fBuf[512];
    while(fgets(fBuf, 512, f) != NULL) {
        if(!strcmp(usr, strtok(fBuf, ";"))) {
            auth = !strcmp(pwd, strtok(fBuf, ";"));
        }
    }

    fclose(f);
    return auth;
}

int main(void) {
    char c;
    int i = 0;
    char buffer[512];
    int len = atoi(getenv("CONTENT_LENGTH"));

    while ((c = getchar()) != EOF && i < len) {
        if (i < 512) {
            if (c!='+') buffer[i] = c;
            else buffer[i]=' ';
            i++;
        }
    }
    buffer[i] = '\0';

    char *delim = "=&";
    char usr[256], pwd[256];

    strtok(buffer, delim);
    strcpy(usr, strtok(NULL, delim));
    strtok(NULL, delim);
    strcpy(pwd, strtok(NULL, delim));

    RESP_HTML_START;

    if(isAuth(usr, pwd)) {
        printf("<h2>Thank you for logging in!</h2>");
        printf("<p>You can now<a href=\"./dashboard.py?username=%s\"><a/>.</p>\n", usr);
    } else {
        printf("<h2>Whoops, you entered your username or password wrong.</h2>");
        printf("<p>Please <a href='../login.html'>try again</a>.</p>\n");
    }

    RESP_HTML_END;
}