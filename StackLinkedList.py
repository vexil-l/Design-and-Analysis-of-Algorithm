class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.is_empty():
            popped_item = self.top.data
            self.top = self.top.next
            return popped_item
        else:
            print("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.top.data
        else:
            print("Stack is empty")

    def size(self):
        count = 0
        current = self.top
        while current:
            count += 1
            current = current.next
        return count

# Example usage:
stack_linked_list = StackLinkedList()
stack_linked_list.push(1)
stack_linked_list.push(2)
stack_linked_list.push(3)

print("\nStack using Linked List:")
print("Pop:", stack_linked_list.pop())
print("Peek:", stack_linked_list.peek())
print("Size:", stack_linked_list.size())
