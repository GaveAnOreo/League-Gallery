#1
def sum_to_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

n = int(input("Enter a number: "))
print(f"The sum of numbers from 1 to {n} is: {sum_to_n(n)}")


#2
def print_number_pattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

n = int(input("Enter the number of rows: "))
print_number_pattern(n)


#3
def fibonacci_series(terms):
    a, b = 0, 1
    for i in range(terms):
        print(a, end=" ")
        a, b = b, a + b
    print()

fibonacci_series(10)


#4
def count_digits(number):
    count = 0
    while number > 0:
        count += 1
        number //= 10
    return count

number = int(input("Enter a number: "))
print(f"Total digits in {number}: {count_digits(number)}")


#5
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n = int(input("Enter a number to find its factorial: "))
print(f"The factorial of {n} is: {factorial(n)}")
