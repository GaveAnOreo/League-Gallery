#include <stdio.h>

void displayPrimeFactors(int n) {
    printf("Prime factors are: ");

    printf("1 ");

    while (n % 2 == 0) {
        printf("%d ", 2);
        n = n / 2;
    }

    for (int i = 3; i * i <= n; i = i + 2) {
        while (n % i == 0) {
            printf("%d ", i);
            n = n / i;
        }
    }

    if (n > 2) {
        printf("%d ", n);
    }
}

int main() {
    int num;

    printf("Enter non-negative number: ");
    if (scanf("%d", &num) != 1 || num < 0) {
        printf("Invalid input. Please enter a non-negative integer.\n");
        return 1;
    }

    displayPrimeFactors(num);

    return 0;
}