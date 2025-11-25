#include <stdio.h>

int main() {
    int number;

    printf("Enter an integer: ");
    scanf("%d", &number);

    if (number % 2 == 0) {
        printf("%d is even.\n", number);
    } else {
        printf("%d is odd.\n", number);
    }

    switch (number % 2) {
        case 0:
            printf("Using switch: %d is even.\n", number);
            break;
        case 1:
            printf("Using switch: %d is odd.\n", number);
            break;
    }

    if (number > 0) {
        if (number % 2 == 0) {
            printf("Using nested if: %d is a positive even number.\n", number);
        } else {
            printf("Using nested if: %d is a positive odd number.\n", number);
        }
    } else if (number < 0) {
        printf("Using nested if: %d is a negative number.\n", number);
    } else {
        printf("Using nested if: %d is zero.\n", number);
    }

    return 0;
}