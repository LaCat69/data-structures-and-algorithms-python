class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current
        self.tail = new_node
    
    def delete(self, value):
        current_left, current_right = self.head, self.tail
        if value == current_left.data:
            self.head = current_left.next
            current_left.next.prev = None
            return
        if value == current_right.data:
            self.tail = current_right.prev
            current_right.prev.next = None
            return
        current = self.head
        while current:
            if current.data == value:
                current.next.prev = current.prev
                current.prev.next = current.next
                return
            current = current.next

    def print_backward(self):
        current = self.tail
        while current:
            print(f"{current.data}", end=" ")
            current = current.prev

node = DoubleLinkedList()

node.append(1)
node.append(2)
node.append(3)

node.print_backward()

print()
node.append(4)
node.print_backward()
node.delete(1)
node.delete(4)
print()
node.print_backward()
node.append(4)
node.append(5)
print()
node.print_backward()
node.delete(4)
node.delete(3)
print()
node.print_backward()