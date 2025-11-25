#include <stdio.h>

struct Coin {
    char *name;
    float value;
    int quantity;
};

float calculateTotalCoinValue(struct Coin coins[], int numCoins) {
    float totalValue = 0;
    int totalCoins = 0;
    for (int i = 0; i < numCoins; i++) {
        totalValue += coins[i].value * coins[i].quantity;
        totalCoins += coins[i].quantity;
    }
    printf("\nYou have a total of %d coins amounting to Php %.2f\n", totalCoins, totalValue);
    return totalValue;
}

int main() {
    struct Coin coins[] = {
        {"ten-peso coin", 10.0, 0},
        {"five-peso coin", 5.0, 0},
        {"one peso coin", 1.0, 0},
        {"twenty-five centavo coin", 0.25, 0}
    };

    int numCoins = sizeof(coins) / sizeof(coins[0]);
    float totalAmount = 0;

    printf("Enter number of coins per value:\n");
    for (int i = 0; i < numCoins; i++) {
        printf("%s: ", coins[i].name);
        if (scanf("%d", &coins[i].quantity) != 1) {
            printf("Invalid input. Please enter an integer.\n");
            return 1;
        }
    }

    totalAmount = calculateTotalCoinValue(coins, numCoins);

    return 0;
}