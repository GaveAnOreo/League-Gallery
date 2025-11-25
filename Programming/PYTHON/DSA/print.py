class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_list(head):
    if head is None:
        print("The linked list is empty.")
        return
    
    current = head
    while current:
        print(current.data)
        current = current.next

head = Node(5)
head.next = Node(10)
head.next.next = Node(15)

print("Linked List:")
print_list(head)
