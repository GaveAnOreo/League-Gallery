#include <iostream>
#include <string>
using namespace std;

int main() {

    string userFirstName, userLastName;
    int userEnrolmentYear;

    cout << "Enter your first name: ";
    cin >> userFirstName;

    cout << "Enter your last name: ";
    cin >> userLastName;

    cout << "Enter your enrolment year: ";
    cin >> userEnrolmentYear;

    const string myFirstName = "Benedict";
    const string myLastName = "Orio";
    const int myEnrolmentYear = 2023;

    if (userFirstName == myFirstName && userLastName == myLastName) {
        cout << "You and I have the same name!" << endl;
    } 

    else if (userFirstName == myFirstName) {
        cout << "We have the same first name!" << endl;
    } 

    else if (userLastName == myLastName) {
        cout << "We have the same last name!" << endl;
    }

    if (userEnrolmentYear > myEnrolmentYear) {
        cout << "Your full name is: " << userFirstName << " " << userLastName << endl;
    }

    return 0;
}