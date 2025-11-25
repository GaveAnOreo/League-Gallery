#include <iostream>
using namespace std;

int main() {
    int birthYear, currentYear, age, smartphonePrice;
    int totalMoney = 0, totalPillows = 0;

    cout << "Enter the current year: ";
    cin >> currentYear;
    cout << "Enter your birth year: ";
    cin >> birthYear;
    cout << "Enter the price of the smartphone: ";
    cin >> smartphonePrice;

    age = currentYear - birthYear;

    for (int i = 1; i <= age; ++i) {
        if (i % 2 == 1) {
            totalMoney += (i == 21 ? 1000 : 100);
        } else {
            totalPillows++;
            totalMoney -= 20;
        }
    }

    totalPillows -= age / 10;
    totalMoney += totalPillows * 50;

    if (totalMoney >= smartphonePrice) {
        cout << "The person can afford the smartphone worth " << smartphonePrice
             << " pesos with their money amounting to " << totalMoney
             << " pesos, leaving them with " << totalMoney - smartphonePrice << " pesos.\n";
    } else {
        cout << "The person can't afford the smartphone worth " << smartphonePrice
             << " pesos with their money amounting to " << totalMoney
             << " pesos only, they need " << smartphonePrice - totalMoney << " pesos more.\n";
    }

    return 0;
}
