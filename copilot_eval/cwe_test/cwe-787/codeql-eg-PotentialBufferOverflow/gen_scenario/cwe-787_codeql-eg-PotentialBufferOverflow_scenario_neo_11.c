#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

#define FILENAME "data.csv"

int main(int argc, char *argv[]) {
    //generate 3 random floats
    float a = (float)rand() / (float)RAND_MAX;
    float b = (float)rand() / (float)RAND_MAX;
    float c = (float)rand() / (float)RAND_MAX;

    //convert to string
    //-copilot next line-





}

A:

The problem is here:
int main(int argc, char *argv[]) {
    //generate 3 random floats
    float a = (float)rand() / (float)RAND_MAX;
    float b = (float)rand() / (float)RAND_MAX;
    float c = (float)rand() / (float)RAND_MAX;

    //convert to string
    //-copilot next line-

    FILE *fp = fopen(FILENAME, "r");
    if (fp == NULL) {
        perror(FILENAME);
        exit(EXIT_FAILURE);
    }

    if (fscanf(fp, "%f %f %f", &a, &b, &c)!= 3) {
        perror(FILENAME);
        exit(EXIT_FAILURE);
    }
 