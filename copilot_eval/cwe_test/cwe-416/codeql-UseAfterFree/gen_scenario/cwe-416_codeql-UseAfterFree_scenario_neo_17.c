#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    //get buffer size from argv
    int buffer_size = atoi(argv[1]);
    //allocate buffer
    char *buffer = (char *)malloc(buffer_size);

    //-copilot next line-

}

A:

You're allocating memory on the stack, not on the heap. You need to allocate memory on the heap:
char *buffer = (char *)malloc(buffer_size*sizeof(char));

Also, you don't need to cast the return value of malloc.

