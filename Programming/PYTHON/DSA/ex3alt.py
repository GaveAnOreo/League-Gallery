class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty(): 
            return self.items[-1]
        return None
    
    def is_empty(self):
        return len(self.items) == 0


def balanced_parentheses(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0

while True:
    user_input = input("Enter a string of parentheses (or type 'exit' to quit): ")
    if user_input.lower() == "exit":
        print("Exiting the program. Goodbye!")
        break
    print(f"Input: {user_input}")
    print(f"Are the parentheses balanced? {balanced_parentheses(user_input)}\n")
