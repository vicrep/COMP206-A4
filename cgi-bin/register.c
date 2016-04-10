#include <stdlib.h>
#include <stdio.h>
#define USR_DATA "./users.txt"

int main(void) {
    char Buffer[512];
    int InputLength = atoi( getenv("INPUT_LENGTH") );
    fread( Buffer, InputLength, 1, stdin );



    printf("Content-type: text/html\n\n");
    printf("<HTML><BODY>\n");
    printf("<P>Hey! This is my first CGI response!</P>\n");
    printf("<pre>%s</pre>\n", Buffer);
    printf( "</BODY></HTML>\n");

    return 0;

}