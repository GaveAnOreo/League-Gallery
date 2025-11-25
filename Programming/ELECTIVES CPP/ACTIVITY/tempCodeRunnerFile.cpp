#include <iostream>
#include <string>
#include <iomanip>
using namespace std;

void printCentered(string text, int lineWidth = 40)
{
    int padding = (lineWidth - text.length()) / 2;  
    if (padding < 0) padding = 0;
    cout << string(padding, ' ') << text << "\n";
}

void printCart(int cartCounter, string cart[], int cartQuantities[])
{
    cout << "\nYour Cart:\n";
    for (int i = 0; i < cartCounter; i++) {
        cout << left << setw(5) << cartQuantities[i] 
             << setw(20) << cart[i] << "\n";
    }
}

int main()
{
    string isDineIn;
    string beverages[] = {"Espresso", "Latte", "Cappuccino", "Americano"};
    double beveragePrices[] = {150.00, 200.50, 220.75, 140.50};
    string food[] = {"Croissant", "Bagel", "Sandwich", "Wrap"};
    double foodPrices[] = {80.00, 60.00, 120.00, 100.00};
    string desserts[] = {"Cake", "Pie", "Ice Cream", "Brownie"};
    double dessertPrices[] = {90.00, 85.00, 70.00, 75.00};

    printCentered("Welcome to Our Cafe!");

    string cart[100];
    double cartPrices[100];
    int cartQuantities[100];
    int cartCounter = 0;
    char choice;

    do {
        int categoryChoice, itemChoice;
        cout << "\nSelect a category (1-Beverages, 2-Food, 3-Desserts): ";
        cin >> categoryChoice;

        if (categoryChoice == 1) {

            cout << "\nBeverages:\n";
            for (int i = 0; i < 4; i++) {
                cout << "[" << i + 1 << "] " << beverages[i] << " - " << fixed << setprecision(2) << beveragePrices[i] << "\n";
            }
            cout << "Select an item: ";
            cin >> itemChoice;
            cart[cartCounter] = beverages[itemChoice - 1];
            cartPrices[cartCounter] = beveragePrices[itemChoice - 1];
            cartQuantities[cartCounter] = 1;
        } else if (categoryChoice == 2) {

            cout << "\nFood:\n";
            for (int i = 0; i < 4; i++) {
                cout << "[" << i + 1 << "] " << food[i] << " - " << fixed << setprecision(2) << foodPrices[i] << "\n";
            }
            cout << "Select an item: ";
            cin >> itemChoice;
            cart[cartCounter] = food[itemChoice - 1];
            cartPrices[cartCounter] = foodPrices[itemChoice - 1];
            cartQuantities[cartCounter] = 1;
        } else if (categoryChoice == 3) {

            cout << "\nDesserts:\n";
            for (int i = 0; i < 4; i++) {
                cout << "[" << i + 1 << "] " << desserts[i] << " - " << fixed << setprecision(2) << dessertPrices[i] << "\n";
            }
            cout << "Select an item: ";
            cin >> itemChoice;
            cart[cartCounter] = desserts[itemChoice - 1];
            cartPrices[cartCounter] = dessertPrices[itemChoice - 1];
            cartQuantities[cartCounter] = 1;
        } else {
            cout << "Invalid category choice.\n";
            continue;
        }

        cartCounter++;
        
        printCart(cartCounter, cart, cartQuantities);

        cout << "Do you want to add more items? (y/n): ";
        cin >> choice;
    } while (choice == 'y' || choice == 'Y');

    cout << "----------------------------------------\n";

    double total = 0;
    for (int i = 0; i < cartCounter; i++)
    {
        cout << left << setw(10) << cartQuantities[i] << setw(20) << cart[i] << setw(10) << fixed << setprecision(2) << cartPrices[i] * cartQuantities[i] << "\n";
        total += cartPrices[i] * cartQuantities[i];
    }

    cout << "----------------------------------------\n";
    cout << "Is this for dine-in or take-out? (d/t): ";
    cin >> isDineIn;
    string word = (isDineIn == "d") ? "Dine in" : "Take out";
    cout << setw(30) << word + " total: " << fixed << setprecision(2) << total << "\n";

    cout << "\n\n---------------------------------------\n\n";
    printCentered("ESB", 40);
    printCentered("PUP STC", 40);
    cout << "\n---------------------------------------\n";
    printCentered("I N V O I C E", 40);
    cout << "\n" << left << setw(5) << "Qty" << setw(25) << "Desc" << setw(10) << "Amnt" << "\n";

    for (int i = 0; i < cartCounter; i++)
    {
        cout << left << setw(5) << cartQuantities[i] << setw(25) << cart[i] << setw(10) << fixed << setprecision(2) << cartPrices[i] * cartQuantities[i] << "\n";
    }

    cout << "\n---------------------------------------\n";
    cout << word << " total:\t\t\t" << fixed << setprecision(2) << total << "\n\n";

    printCentered("Thank you for visiting ESB!", 40);

    return 0;
}