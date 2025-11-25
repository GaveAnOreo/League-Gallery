#include <iostream>
#include <limits> // For input validation
#include <cctype> // For isdigit()
using namespace std;

// Function to check if a string represents a valid integer
bool isValidInteger(const string& input) {
    for (char ch : input) {
        if (!isdigit(ch)) {
            return false;
        }
    }
    return true;
}

// Function to check if a string represents a valid double
bool isValidDouble(const string& input) {
    bool decimalFound = false;
    for (char ch : input) {
        if (!isdigit(ch)) {
            if (ch == '.' && !decimalFound) {
                decimalFound = true; // Allow one decimal point
            } else {
                return false; // Reject any other non-digit character
            }
        }
    }
    return true;
}

int main() {
    int choice;
    double value;
    string again;
    string prompt;
    string input;

    do {
        cout << "1. Inches to Centimeters\n";
        cout << "2. Centimeters to Inches\n";
        cout << "3. Pounds to Kilograms\n";
        cout << "4. Kilograms to Pounds\n";
        cout << "5. Fahrenheit to Celsius\n";
        cout << "6. Celsius to Fahrenheit\n";
        cout << "7. Feet to Meters\n";
        cout << "8. Meters to Feet\n";
        cout << "9. Gallons to Liters\n";
        cout << "10. Liters to Gallons\n";
        cout << "11. Miles to Kilometers\n";
        cout << "12. Kilometers to Miles\n";
        cout << "13. Square Feet to Square Meters\n";
        cout << "14. Square Meters to Square Feet\n";
        cout << "15. PSI to Bar\n";
        cout << "16. Bar to PSI\n";
        cout << "17. Joules to Calories\n";
        cout << "18. Calories to Joules\n";
        cout << "19. Megabytes to Gigabytes\n";
        cout << "20. Gigabytes to Megabytes\n";

        // Validate choice input
        while (true) {
            cout << "Enter your choice (1-20): ";
            cin >> input;
            if (isValidInteger(input)) {
                choice = stoi(input); // Convert to integer
                if (choice >= 1 && choice <= 20) {
                    break; // Valid input, exit the loop
                }
            }
            cout << "Invalid choice!\n";
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
        }

        // Determine the prompt based on the choice
        switch (choice) {
            case 1: prompt = "Enter a value in inches: "; break;
            case 2: prompt = "Enter a value in centimeters: "; break;
            case 3: prompt = "Enter a value in pounds: "; break;
            case 4: prompt = "Enter a value in kilograms: "; break;
            case 5: prompt = "Enter a value in Fahrenheit: "; break;
            case 6: prompt = "Enter a value in Celsius: "; break;
            case 7: prompt = "Enter a value in feet: "; break;
            case 8: prompt = "Enter a value in meters: "; break;
            case 9: prompt = "Enter a value in gallons: "; break;
            case 10: prompt = "Enter a value in liters: "; break;
            case 11: prompt = "Enter a value in miles: "; break;
            case 12: prompt = "Enter a value in kilometers: "; break;
            case 13: prompt = "Enter a value in square feet: "; break;
            case 14: prompt = "Enter a value in square meters: "; break;
            case 15: prompt = "Enter a value in PSI: "; break;
            case 16: prompt = "Enter a value in bar: "; break;
            case 17: prompt = "Enter a value in joules: "; break;
            case 18: prompt = "Enter a value in calories: "; break;
            case 19: prompt = "Enter a value in megabytes: "; break;
            case 20: prompt = "Enter a value in gigabytes: "; break;
        }

        // Validate value input with the same prompt
        while (true) {
            cout << prompt;
            cin >> input;
            if (isValidDouble(input)) {
                value = stod(input); // Convert to double
                break; // Valid input, exit the loop
            } else {
                cout << "Invalid input!\n";
                cin.clear();
                cin.ignore(numeric_limits<streamsize>::max(), '\n');
            }
        }

        // Perform the conversion and display the result
        switch (choice) {
            case 1: cout << value << " inches = " << value * 2.54 << " cm\n"; break;
            case 2: cout << value << " cm = " << value / 2.54 << " inches\n"; break;
            case 3: cout << value << " pounds = " << value * 0.453592 << " kg\n"; break;
            case 4: cout << value << " kg = " << value / 0.453592 << " pounds\n"; break;
            case 5: cout << value << "°F = " << (value - 32) * 5 / 9 << "°C\n"; break;
            case 6: cout << value << "°C = " << (value * 9 / 5) + 32 << "°F\n"; break;
            case 7: cout << value << " feet = " << value * 0.3048 << " meters\n"; break;
            case 8: cout << value << " meters = " << value / 0.3048 << " feet\n"; break;
            case 9: cout << value << " gallons = " << value * 3.78541 << " liters\n"; break;
            case 10: cout << value << " liters = " << value / 3.78541 << " gallons\n"; break;
            case 11: cout << value << " miles = " << value * 1.60934 << " km\n"; break;
            case 12: cout << value << " km = " << value / 1.60934 << " miles\n"; break;
            case 13: cout << value << " sq ft = " << value * 0.092903 << " sq m\n"; break;
            case 14: cout << value << " sq m = " << value / 0.092903 << " sq ft\n"; break;
            case 15: cout << value << " PSI = " << value * 0.0689476 << " bar\n"; break;
            case 16: cout << value << " bar = " << value / 0.0689476 << " PSI\n"; break;
            case 17: cout << value << " joules = " << value * 0.239006 << " calories\n"; break;
            case 18: cout << value << " calories = " << value / 0.239006 << " joules\n"; break;
            case 19: cout << value << " MB = " << value / 1024 << " GB\n"; break;
            case 20: cout << value << " GB = " << value * 1024 << " MB\n"; break;
        }

        // Validate "again" input
        while (true) {
            cout << "Do another conversion? (y/n): ";
            cin >> again;
            cin.ignore(numeric_limits<streamsize>::max(), '\n'); // Clear the buffer
            if (again.length() == 1 && (again[0] == 'y' || again[0] == 'Y' || again[0] == 'n' || again[0] == 'N')) {
                break;
            } else {
                cout << "Invalid input!\n";
            }
        }

    } while (again[0] == 'y' || again[0] == 'Y');

    cout << "Thank you!\n";
    return 0;
}