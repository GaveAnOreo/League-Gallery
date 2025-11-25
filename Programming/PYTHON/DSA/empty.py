class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def is_empty(head):
    if head is None:
        return True
    else:
        return False

head = None
print("The linked list is empty." if is_empty(head) else "The linked list is not empty.")
