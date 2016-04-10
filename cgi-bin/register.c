#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#define USR_DATA "users.txt"
#define RESP_HTML_START printf("Content-type: text/html\n\n<html><head><link rel=\"stylesheet\" type=\"text/css\" href=\"../css/main.css\"></head><body>\n")
#define RESP_HTML_END printf("\n</body></html>\n")
#define BOOL int
#define TRUE 1
#define FALSE 0

struct User {
    char    name[256];
    char    job[256];
    char    username[256];
    char    pwd[256];
} usr;


BOOL verifyUser() {
    FILE *f = fopen(USR_DATA, "r");

    char fBuf[512];
    while(fgets(fBuf, 512, f) != NULL) {
        if(!strcmp(usr.username, strtok(fBuf, ";"))) {
            fclose(f);
            return FALSE;
        }
    }

    fclose(f);
    return TRUE;
}

void addUser() {
    FILE *f = fopen(USR_DATA, "a");
    fprintf(f, "%s;%s;%s;%s", usr.username, usr.pwd, usr.name, usr.job);
    fclose(f);
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
    strtok(buffer, delim);
    strcpy(usr.name, strtok(NULL, delim));
    strtok(NULL, delim);
    strcpy(usr.job, strtok(NULL, delim));
    strtok(NULL, delim);
    strcpy(usr.username, strtok(NULL, delim));
    strtok(NULL, delim);
    strcpy(usr.pwd, strtok(NULL, delim));

    RESP_HTML_START;
    if(verifyUser()) {
        addUser();
        printf("<h3>Thank you for signing up, %s!</h2>\n", usr.name);
        printf("<p>You may now <a href='../login.html'>log in</a>.</p>\n");
    } else {
        printf("<h3>Sorry, there already exists a user with the username: %s</h3>\n", usr.username);
        printf("<p>Please <a href='../login.html'>try again</a>.</p>\n");
    }
    RESP_HTML_END;

    exit(0);
}