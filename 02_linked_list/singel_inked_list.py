class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(5)
node2 = Node(15)
node3 = Node(25)
node4 = Node(35)

node1.next = node2
node2.next = node3
node3.next = node4

current = node1
while current:
    print(current.data)
    current = current.next

#####################################################

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    
    def find(self, value):
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False
    
    def delete(self, value):
        current = self.head
        if current and current == value:
            self.head = current.next
            return
        prev = None
        while current:
            if current.data == value:
                prev.next = current.next
                return
            prev = current
            current = current.next

node = LinkedList()
node.append(1)
node.append(2)
node.append(3)
node.append(4)
node.append(5)

node.print_list()

print(node.find(3))
node.delete(2)

node.print_list()