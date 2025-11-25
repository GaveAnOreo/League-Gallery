class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def is_empty(head):
    return head is None

head = None
print("The linked list is empty." if is_empty(head) else "The linked list is not empty.")
