class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_list(head):
    if not head:
        print("The linked list is empty.")
        return
    
    current = head
    while current:
        print(current.data)
        current = current.next

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

print("Linked List:")
print_list(head)