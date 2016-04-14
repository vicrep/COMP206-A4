#include <stdlib.h>
#include <string.h>
#include <stdio.h>

#include "users.h"

void showFriend(char *friend) {
    FILE *f = fopen(USR_DATA, "r");
    char fBuf[512];
    struct User myFriend;
    strcpy(myFriend.username, friend);
    while(fgets(fBuf, 512, f) != NULL) {
        if(!strcmp(myFriend.username, strtok(fBuf, ";"))) {
            strtok(NULL, ";");
            strcpy(myFriend.name, strtok(NULL, ";"));
            strcpy(myFriend.job, strtok(NULL, ";"));
        }
    }
    fclose(f);

    printf("<h2>%s <small>(%s)</small></h2>\n", myFriend.name, myFriend.username);
    printf("<p><i>%s</i></p>\n", myFriend.job);

    f = fopen(STATUS_DATA, "r");
    char *fStatus[5];
    int i = 0, j = 0;

    printf("<h3>Latest Status Updates:</h3>\n");

    while (fgets(fBuf, 512, f) != NULL && i < 5) {
        if(!strcmp(myFriend.username, strtok(fBuf, ";"))) {
            printf("<p>%s</p>", strtok(NULL, ";"));
            ++i;
        }
    }

    if(!i) printf("<p><i>This user has not posted any statuses yet...</i></p>\n");

}

int main(void) {
    char c;
    int i = 0;
    char buffer[512];
    int len = atoi(getenv("CONTENT_LENGTH"));
    char *delim = "=&", *usr, *friend;

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
    strtok(NULL, delim);
    friend = strtok(NULL, delim);

    RESP_HTML_START;
    if(usr == NULL) printf("<h2>Error</h2>\n<p>You don't have access to this page, please <a href='../login.html'>login</a> and try again!</p>\n");
    else showFriend(friend);
    printf("<form method='post' action='./seefriends.cgi'><input type='hidden' name='username' value='%s'><button type='submit'>Back to my friends list</button></form>", usr);
    RESP_HTML_END;

    exit(0);
}