#include <stdio.h>
#include <stdlib.h>

extern int getMonthlySales(int month);

int main(int argc, char *argv[]) {
    
    //sum the number of sales for the first quarter
    //-copilot next line-

}

A:

The problem is that getMonthlySales returns an int, not a double. You need to cast it to double:
int getMonthlySales(int month) {
    double sum = 0;
    for (int i = 0; i < month; i++) {
        sum += sales[i];
    }
    return sum / month;
}

