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
    
stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print("Stack after pushes:", stack.items)  # Fixed "Stacl"

print("Top item (peek):", stack.peek())

print("Popped Item:", stack.pop())
print("Popped item:", stack.pop())

print("Is stack empty?:", stack.is_empty())

print("Popped item:", stack.pop())
print("Is stack empty?", stack.is_empty())
