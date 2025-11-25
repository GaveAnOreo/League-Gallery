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
    
def reverse_string(s):
    stack = Stack()
    for char in s:
        stack.push(char)
    
    reversed_str = ""
    while not stack.is_empty():
        reversed_str += stack.pop()
    
    return reversed_str

input_string = input("Please input a string to reverse: ")
reverse_result = reverse_string(input_string)
print("Reversed: ", reverse_result)