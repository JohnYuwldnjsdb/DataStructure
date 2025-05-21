class Node:
    def __init__(self, key, value, height, left=None, right=None):
        self.key = key
        self.value = value
        self.height = height
        self.left = left
        self.right = right

class AVL:
    def __init__(self):
        self.root = None
    
    def height(self, n):
        if n is None:
            return 0
        
        return n.height
    
    def get(self, key):
        return self.get_item(self.root, key)

    def get_item(self, n, k):
        if n is None:
            return None
        
        if n.key > k:
            return self.get_item(n.left, k)
        elif n.key < k:
            return self.get_item(n.right, k)
        else:
            return n.value
    
    def put(self, key, value):
        self.root = self.put_item(self.root, key, value)

    def put_item(self, n, key, value):
        if n is None:
            return Node(key, value, 1)

        if n.key > key:
            n.left = self.put_item(n.left, key, value)
        elif n.key > key:
            n.left = self.put_item(n.right, key, value)
        else:
            n.value = value
            return n
        
        n.height = max(self.height(n.left), self.height(n.right)) + 1
        return self.balance(n)

    def balance(self, n):
        if self.bf(n) > 1:
            if self.bf(n.left) < 0:
                n.left = self.rotate_left(n.left)
            return self.rotate_right(n)
        elif self.bf(n) < -1:
            if self.bf(n.right) > 0:
                n.right = self.rotate_right(n.right)
            return self.rotate_left(n)
        return n
    
    def bf(self, n):
        pass

    def rotate_right(self, n):
        x = n.left
        n.left = x.right
        x.right = n
        n.height = max(self.height(n.left), self.height(n.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        return x
    
    def rotate_left(self, n):
        x = n.right
        n.right = x.left
        x.left = n
        n.height = max(self.height(n.left), self.height(n.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        return x
    
    def delete(self, key):
        pass

    def delete_min(self):
        pass
    
    def min(self):
        pass

t = AVL()
