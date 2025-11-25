#include <iostream>
#include <string>

int main() {
    std::string name = "benedict";
    int length = name.size();

    for (int i = 0; i < length; ++i) {
        std::cout << std::string(length - i - 1, ' ');
        std::cout << std::string(2 * i + 1, name[i]) << std::endl;
    }

    return 0;
}