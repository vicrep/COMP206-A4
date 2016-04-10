#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#define USR_DATA "users.txt"
#define RESP_HTML_START printf("Content-type: text/html\n\n<html><body>\n")
#define RESP_HTML_END printf("\n</body></html>\n")
#define BOOL int
#define TRUE 1
#define FALSE 0

struct User {
    char    name[256];
    char    job[256];
    char    username[256];
    char    pwd[256];
};


BOOL addUser(struct User usr) {
    FILE *f = fopen(USR_DATA, "+a");

    char tmp[512];
    while(fgets(tmp, 512, f) != EOF) {
        char* username;
         username = strtok(tmp, ";");
        if (!strcmp(username, usr.username)) return FALSE;
    };

    fprintf(f, "%s;%s;%s;%s\n", usr.username, usr.pwd, usr.name, usr.job);
    fclose(f);

    return TRUE;
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

    struct User usr;

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
//    if(addUser(usr)) {
//        printf("<h3>Thank you for signing up!</h2>\n");
//        printf("<p>You may now <a href='../login.html'>log in</a>.</p>\n");
//    } else {
//        printf("<h3>Sorry, there already exists a user with the username: %s</h3>\n", usr.username);
//        printf("<p>Please <a href='../login.html'>try again</a>.</p>\n");
//    }
    printf("<ul><li>%s</li><li>%s</li><li>%s</li><li>%s</li></ul>", usr.name, usr.username, usr.job, usr.pwd);
    RESP_HTML_END;

    exit(0);
}