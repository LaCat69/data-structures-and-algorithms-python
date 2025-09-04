class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.tail:
            self.head = new_node
            self.tail = new_node
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def appendleft(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
    
    def pop(self):
        if not self.tail:
            return None
        if self.tail == self.head:
            current = self.head
            self.head = None
            self.tail = None
            return current.data
        current = self.tail
        self.tail = current.prev
        self.tail.next = None
        return current.data
    
    def popleft(self):
        if not self.head:
            return None
        if self.tail == self.head:
            current = self.head
            self.head = None
            self.tail = None
            return current.data
        current = self.head
        self.head = current.next
        self.head.prev = None
        return current.data


    def printright(self):
        current = self.head
        while current:
            print(f"{current.data}", end=" -> ")
            current = current.next
        print("None")
    
    def printleft(self):
        current = self.tail
        while current:
            print(f"{current.data}", end=" -> ")
            current = current.prev
        print("None")

dq = Deque()
dq.appendleft(2)
dq.append(3)
dq.appendleft(1)
dq.printright()
dq.printleft()
print(dq.pop())
dq.printright()
dq.printleft()
dq.append(3)
dq.append(4)
print(dq.popleft())
dq.printleft()
dq.printright()