#define USR_DATA "users.txt"
#define FRIEND_DATA "friends.txt"
#define STATUS_DATA "status.txt"
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
};
