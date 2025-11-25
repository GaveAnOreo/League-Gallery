#include <stdio.h>

int convertHoursToMinutes(int hours) {
    return hours * 60;
}

int main() {
    int hours;
    
    printf("Enter the number of hours: ");
    if (scanf("%d", &hours) != 1 || hours < 0) {
        printf("Invalid input. Please enter a non-negative integer.\n");
        return 1;
    }

    int minutes = convertHoursToMinutes(hours);

    printf("%d hours are equal to %d minutes.\n", hours, minutes);

    return 0;
}