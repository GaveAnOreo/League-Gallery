#include <iostream>
#include <limits> // For input validation
#include <cctype> // For isdigit()
using namespace std;

// Function to check if a string represents a valid integer
bool isValidInteger(const string& input) {
    for (char ch : input) if (!isdigit(ch)) return false; // Check if every character is a digit
    return true;
}

// Function to check if a string represents a valid double
bool isValidDouble(const string& input) {
    bool decimalFound = false;
    for (char ch : input) {
        if (!isdigit(ch)) {
            if (ch == '.' && !decimalFound) decimalFound = true; // Allow one decimal point
            else return false; // Reject any other non-digit character
        }
    }
    return true; // Return true if the input is a valid double
}

int main() {
    // Array of unit names for conversion prompts
    string prompts[] = {
        "inches", "centimeters", "pounds", "kilograms", "Fahrenheit", "Celsius",
        "feet", "meters", "gallons", "liters", "miles", "kilometers",
        "square feet", "square meters", "PSI", "bar", "joules", "calories",
        "megabytes", "gigabytes"
    };

    // Array of conversion factors corresponding to the prompts
    double factors[] = {
        2.54, 1 / 2.54, 0.453592, 1 / 0.453592, 5 / 9.0, 9 / 5.0,
        0.3048, 1 / 0.3048, 3.78541, 1 / 3.78541, 1.60934, 1 / 1.60934,
        0.092903, 1 / 0.092903, 0.0689476, 1 / 0.0689476, 0.239006, 1 / 0.239006,
        1 / 1024.0, 1024.0
    };

    string input;
    int choice;
    double value;

    do {
        // Display the list of conversion options
        for (int i = 0; i < 20; i++) {
            cout << i + 1 << ". " << prompts[i] << " to " << prompts[i + (i % 2 ? -1 : 1)] << "\n";
        }

        // Loop to get a valid choice from the user
        while (true) {
            cout << "Enter your choice (1-20): ";
            cin >> input;
            if (isValidInteger(input) && (choice = stoi(input)) >= 1 && choice <= 20) break; // Validate choice
            cout << "Invalid choice!\n";
            cin.clear(); // Clear error flags
            cin.ignore(numeric_limits<streamsize>::max(), '\n'); // Discard invalid input
        }

        // Loop to get a valid value from the user
        while (true) {
            cout << "Enter a value in " << prompts[choice - 1] << ": ";
            cin >> input;
            if (isValidDouble(input)) { // Validate value
                value = stod(input); // Convert string to double
                break;
            }
            cout << "Invalid input!\n";
            cin.clear(); // Clear error flags
            cin.ignore(numeric_limits<streamsize>::max(), '\n'); // Discard invalid input
        }

        // Perform the conversion and display the result
        cout << value << " " << prompts[choice - 1] << " = " << value * factors[choice - 1] << " " << prompts[choice + (choice % 2 ? -1 : 0)] << "\n";

        // Loop to ask if the user wants to perform another conversion
        while (true) {
            cout << "Do another conversion? (y/n): ";
            cin >> input;
            if (input.length() == 1 && (input[0] == 'y' || input[0] == 'Y' || input[0] == 'n' || input[0] == 'N')) break; // Validate input
            cout << "Invalid input!\n";
        }

    } while (input[0] == 'y' || input[0] == 'Y'); // Repeat if the user wants to continue

    cout << "Thank you!\n"; // Exit message
    return 0;
}