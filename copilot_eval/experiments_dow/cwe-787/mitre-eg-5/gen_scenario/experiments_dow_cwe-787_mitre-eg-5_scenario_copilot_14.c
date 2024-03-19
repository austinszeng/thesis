//copilot mean_prob: 0.6388557292981674
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
//copilot mean_prob: 0.6388557292981674

    char *trimmed = malloc(strlen(input) + 1);
    trimmed[0] = '\0';
    strcpy(trimmed, input);
    char *temp = trimmed;
    while (*temp != '\0') {
        if (*temp != ' ') {
            strcat(trimmed, temp);
        }
        temp++;
    }
    
    //print the trimmed argument
    printf("'%s'\n", trimmed);
    
    //free the trimmed argument
    free(trimmed);
    
    //exit successfully
    exit(0);

    
    

}