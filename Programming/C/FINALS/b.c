#include <stdio.h>

char determineCategory(int age) {
    if (age >= 0 && age <= 12) {
        return 'C';
    } else if (age >= 13 && age <= 19) {
        return 'T';
    } else if (age >= 20) {
        return 'A';
    }
    
}

int main() {
    int age;

    printf("Enter age: ");
    if (scanf("%d", &age) != 1) {
        printf("Invalid input. Please enter an integer.\n");
        return 1;
    }

    char category = determineCategory(age);

    switch (category) {
        case 'C':
            printf("Person is a child.\n");
            break;
        case 'T':
            printf("Person is a teenager.\n");
            break;
        case 'A':
            printf("Person is an adult.\n");
            break;
        default:
            printf("Invalid age.\n");
            break;
    }

    return 0;
}