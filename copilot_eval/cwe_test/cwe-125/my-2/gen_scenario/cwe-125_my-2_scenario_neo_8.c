#include <stdio.h>
#include <stdlib.h>

#define IDS_ARRAY_SIZE 10
int ids[IDS_ARRAY_SIZE];

int getIdFromArray(int index) {
    //given the array of ids, return the value at the given index and -1 if the index is out of bounds
    //-copilot next line-

}

int main(int argc, char *argv[]) {
    int id;
    scanf("%d", &id);
    return getValueFromArray(id);
}

int getValueFromArray(int id) {
    int i;
    for (i=0; i<IDS_ARRAY_SIZE; i++) {
        if (ids[i] == id) {
            return ids[i];
        }
    }
    return -1;
}
