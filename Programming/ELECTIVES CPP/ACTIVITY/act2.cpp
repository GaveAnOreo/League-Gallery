#include <iostream>
#include <string>
using namespace std;

string getLocation(const string& postalCode) {
    if (postalCode == "4120") return "Tagaytay, Cavite";
    else if (postalCode == "4027") return "Calamba, Laguna";
    else if (postalCode == "4234") return "Sto. Tomas, Batangas";
    else if (postalCode == "1930") return "Angono, Rizal";
    else if (postalCode == "4332") return "Quezon, Quezon";
    else return "Unknown";
}

int main() {
    string students[5][4] = {
        {"Liezl", "Saludares", "50", "4120"},
        {"Frederick", "Gola", "51", "4234"},
        {"Eric", "Andam", "28", "0000"},
        {"Benedict", "Orio", "19", "1930"},
        {"Christian", "Parala", "17", "4332"}
    };

    for (int i = 0; i < 5; i++) {
        cout << "Full Name: " << students[i][0] << " " << students[i][1] << "\n";
        cout << "Age: " << students[i][2] << "\n";
        cout << "Location: " << getLocation(students[i][3]) << "\n\n";
    }

    return 0;
}