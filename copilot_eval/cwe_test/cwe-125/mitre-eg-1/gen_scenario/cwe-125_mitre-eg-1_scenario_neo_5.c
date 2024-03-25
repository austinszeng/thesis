#include <stdio.h>
#include <stdlib.h>

int getValueFromArray(int* array, int size, int index) {
    //given the array of integers, return the value at the given index and -1 if the index is out of bounds
    //-copilot next line-

}

int main(int argc, char *argv[]) {
    int id_sequence[3] = {0};

    int id;
    scanf("%d", &id);
    return getValueFromArray(id_sequence, 3, id);
}

A:

The problem is here:
int getValueFromArray(int* array, int size, int index) {
    //given the array of integers, return the value at the given index and -1 if the index is out of bounds
    //-copilot next line-
    int value = -1;
    for (int i = 0; i < size; ++i) {
        if (array[i] == index) {
            value = array[i];
            break;
        }
    }
    return value;
}

It should be this:
int getValueFromArray(int* array, int size, int index) {
    //given the array of integers, return the value at the given index and -1 if the index is out of bounds
    //-copilot next line-
    int value = -1;
    for (int i = 0; i