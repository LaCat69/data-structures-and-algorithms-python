class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
    
    def push(self, value):
        new_node = Node(value)
        if not self.top:
            self.top = new_node
            return
        new_node.next, self.top = self.top, new_node

    def pop(self):
        if not self.top:
            return None
        current = self.top
        self.top = self.top.next
        return current.data
    
    def peek(self):
        return self.top.data
    
    def is_empty(self):
        return True if not self.top else False

stack = Stack()
print(stack.is_empty())
print(stack.pop())
stack.push(5)
print(stack.peek())
stack.push(4)
print(stack.peek())
stack.push(3)
print(stack.pop())
print(stack.peek())
print(stack.is_empty())