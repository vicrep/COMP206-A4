#include <stdlib.h>

char str[200];

_len = getenv("CONTENT_LENGTH");
len = strtol(_len, NULL, 10);

data = malloc(len + 1);

if(!data) exit(EXIT_FAILURE);

fgets(data, len + 1, stdin);

free(data);