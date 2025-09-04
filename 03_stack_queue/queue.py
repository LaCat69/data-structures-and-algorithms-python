class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node
    
    def dequeue(self):
        if not self.head:
            return None
        if not self.head.next:
            value = self.head
            self.head = None
            self.tail = None
            return value.data
        value = self.head
        self.head = self.head.next
        return value.data
    
    def peek(self):
        return self.head.data
    
    def is_empty(self):
        return True if not self.head else False

q = Queue()
q.enqueue(1)
print(q.dequeue())
print(q.dequeue())
q.enqueue(2)
q.enqueue(1)
print(q.dequeue())
print(q.peek())
q.dequeue()
print(q.is_empty())