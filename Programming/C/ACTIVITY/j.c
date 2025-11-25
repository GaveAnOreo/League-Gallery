#include <stdio.h>

int main() {
    int rows = 6;

    for (int i = 0; i < rows; i++) {
        int number = 1;

        for (int space = 1; space <= rows - i; space++) {
            printf("   ");
        }

        for (int j = 0; j <= i; j++) {
            printf("%6d", number);

            number = number * (i - j) / (j + 1);
        }

        printf("\n");
    }

    return 0;
}