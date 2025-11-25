print("Enter 'quit' when you are finished adding toppings.")

while True:
    topping = input("Enter a pizza topping: ")
    
    if topping.lower() == 'quit':
        print("All toppings have been added.")
        break
    else:
        print(f"We'll add {topping} to your pizza.")
