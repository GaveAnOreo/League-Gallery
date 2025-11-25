#include <stdio.h>

int main() {
    int num1, num2, num3;

    printf("Enter three numbers: ");
    scanf("%d %d %d", &num1, &num2, &num3);

    if (num1 >= num2 && num1 >= num3) {
        printf("Using if: %d is the largest number.\n", num1);
    }

    if (num2 >= num1 && num2 >= num3) {
        printf("Using if...else: %d is the largest number.\n", num2);
    } else {
        printf("Using if...else: %d is the largest number.\n", num3);
    }

    if (num1 >= num2 && num1 >= num3) {
        printf("Using nested if...else: %d is the largest number.\n", num1);
    } else if (num2 >= num1 && num2 >= num3) {
        printf("Using nested if...else: %d is the largest number.\n", num2);
    } else {
        printf("Using nested if...else: %d is the largest number.\n", num3);
    }

    return 0;\
}