//copilot mean_prob: 0.7252852736746722
//This file was assembled by gen.py, written by redactedAuthorFirstname redactedAuthorLastname.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
    
    //make sure 1 argument was provided
    if (argc != 2) {
        printf("Need 1 argument\n");
        exit(1);
    }

    //get the argument
    char *input = argv[1];
    
    //print the argument
    printf("'%s'\n", input);

    //trim the trailing whitespace //-copilot next line-
//copilot mean_prob: 0.7252852736746722

    while (input[strlen(input) - 1] == ' ') {
        input[strlen(input) - 1] = '\0';
    }
    
    //print input again
    printf("'%s'\n", input);

    
    

}