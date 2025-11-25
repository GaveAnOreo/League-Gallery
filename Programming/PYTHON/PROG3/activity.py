#1. Simple Messages
message = "Hello, this is my first message!"
print(message)

message = "Now, this is my second message."
print(message)

#2. Name Cases
name = "aLbert einsTein"
print(name.lower())
print(name.upper())
print(name.title())

#3. Famous Quote
author = 'Albert Einstein'
quote = 'once said, "A person who never made a mistake never tried anything new."'
print(author + quote)

#4. Adding Comments
# Program 5: Pizzas
# This program stores favorite pizza names in a list and uses a loop to print a message for each pizza.

# List of favorite pizzas
pizzas = ["pepperoni", "margherita", "hawaiian"]

# Loop through the list of pizzas
for pizza in pizzas:
    # Print a message for each pizza
    print(f"I like {pizza} pizza.")

# Print an additional statement about how much I love pizza
print("\nI really love pizza! My favorite kinds are pepperoni, margherita, and hawaiian.")

# Program 6: Counting to Twenty
# This program prints the numbers from 1 to 20 using a for loop.

# Loop through the numbers 1 to 20
for number in range(1, 21):
    # Print each number
    print(number)

#5. Pizzas
pizzas = ["pepperoni", "margherita", "hawaiian"]

for pizza in pizzas:
    print(f"I like {pizza} pizza.")

print("\nI really love pizza! My favorite kinds are pepperoni, margherita, and hawaiian.")

#6. Counting to Twenty
for number in range(1, 21):
    print(number)

#7. Odd Numbers
for number in range(1, 21, 2):
    print(number)

#8. Threes
for number in range(3, 31, 3):
    print(number)

#9. Cubes
for number in range(1, 11):
    cube = number ** 3
    print(f"The cube of {number} is {cube}")
