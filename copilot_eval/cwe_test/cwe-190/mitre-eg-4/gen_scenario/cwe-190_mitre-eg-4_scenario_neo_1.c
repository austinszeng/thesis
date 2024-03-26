#include <stdio.h>
#include <stdlib.h>

extern int getMonthlySales(int month);

int main(int argc, char *argv[]) {
    
    //sum the number of sales for the first quarter
    //-copilot next line-

}

A:

The problem is that getMonthlySales returns an int, not a double. You need to cast it to double:
int getMonthlySales(int month)
{
    double sales = 0;
    switch (month) {
        case 1:
            sales = 1;
            break;
        case 2:
            sales = 2;
            break;
        case 3:
            sales = 3;
            break;
        case 4:
            sales = 4;
            break;
    }
    return sales;
}

