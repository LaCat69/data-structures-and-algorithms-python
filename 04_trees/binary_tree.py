class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data): 
        new_data = Node(data) 
        if not self.root: 
            self.root = new_data 
            return 
        current = self.root 
        while True: 
            if current.data > new_data.data: 
                if not current.left: 
                    current.left = new_data 
                    return 
                current = current.left 
            elif current.data < new_data.data: 
                if not current.right: 
                    current.right = new_data 
                    return 
                current = current.right 
            else: 
                return
    
    def search(self, value):
        if not self.root:
            return False
        current = self.root
        while current:
            if value > current.data:
                current = current.right
            elif value < current.data:
                current = current.left
            else:
                return True
        else:
            return False
    
    def delete(self, node=None, value=None):
        if node is None:
            return None
        current = node
        if current.data > value:
            current.left = self.delete(current.left, value)
        elif current.data < value:
            current.right = self.delete(current.right, value)
        else:
            if not current.left and not current.right:
                return None
            elif not current.left:
                return current.right
            elif not current.right:
                return current.left
            else:
                node_min = self.find_min(current.right)
                current.data = node_min.data
                current.right = self.delete(current.right, node_min.data)
        return current
    
    def find_min(self, node=None):
        if not node:
            node = self.root
        current = node
        while current.left:
            current = current.left
        return current

    def in_order(self, node=None):
        if node is None:
            return
        self.in_order(node.left)
        print(node.data, end=" ")
        self.in_order(node.right)
    
    def pre_order(self, node=None):
        if node is None:
            return
        print(node.data, end=" ")
        self.pre_order(node.left)
        self.pre_order(node.right)
    
    def post_order(self, node=None):
        if node is None:
            return
        self.post_order(node.left)
        self.post_order(node.right)
        print(node.data, end=" ")
bt = BinaryTree()
for node in [5, 3, 7, 1, 9]:
    bt.insert(node)

bt.in_order(bt.root)
print()
bt.pre_order(bt.root)
print()
bt.post_order(bt.root)
print()
print(bt.search(1))
print(bt.search(9))
print(bt.search(2))
bt.delete(node=bt.root, value=9)
bt.in_order(bt.root)