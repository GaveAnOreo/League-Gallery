#include <stdio.h>

int main() {
    int number;

    printf("Enter an integer: ");
    scanf("%d", &number);

    if (number > 0) {
        printf("Using if-else: %d is positive.\n", number);
    } else if (number < 0) {
        printf("Using if-else: %d is negative.\n", number);
    } else {
        printf("Using if-else: %d is zero.\n", number);
    }

    switch (number > 0) {
        case 1:
            printf("Using switch: %d is positive.\n", number);
            break;
        case 0:
            switch (number < 0) {
                case 1:
                    printf("Using switch: %d is negative.\n", number);
                    break;
                case 0:
                    printf("Using switch: %d is zero.\n", number);
                    break;
            }
            break;
    }

    if (number > 0) {
        printf("Using nested if: %d is positive.\n", number);
    } else {
        if (number < 0) {
            printf("Using nested if: %d is negative.\n", number);
        } else {
            printf("Using nested if: %d is zero.\n", number);
        }
    }

    return 0;