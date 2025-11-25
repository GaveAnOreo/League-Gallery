#1
def sum_of_numbers(n):
    return sum(range(1, n+1))

n = int(input("Enter a number: "))
print(f"Sum of all numbers frome 1 to {n} is {sum_of_numbers(n)}")


#2
def number_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()

rows = int(input("Enter number of rows: "))
number_pattern(rows)


#3
def fibonacci(n):
    fib_sequence =[0,1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence
    
terms = 10
print(f"Fibonacci series up to {terms} terms: {fibonacci(terms)}")


#4
def count_digits(num):
    count = 0
    while  num !=0:
        num//= 10
        count += 1
    return count

num = int(input("Enter a number:"))
print(f"Total number of digits in {num} is {count_digits(num)}")


#5
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

n = int(input("Enter a number: "))
print(f"Factorial of {n} is {factorial(n)}")