from collections import deque

class BinaryTree:
    class Node:
        def __init__(self, item, left = None, right = None):
            self.item = item
            self.left = left
            self.right = right
    
    def __init__(self):
        self.root = None
    
    def preorder(self, n):
        if n is not None:
            print(n.item, end=' ')
            if n.left is not None:
                self.preorder(n.left)
            
            if n.right is not None:
                self.preorder(n.right)
    
    def inorder(self, n):
        if n is not None:
            if n.left is not None:
                self.inorder(n.left)
            
            print(n.item, end=' ')
            
            if n.right is not None:
                self.inorder(n.right)
    
    def postorder(self, n):
        if n is not None:
            if n.left is not None:
                self.postorder(n.left)
            
            if n.right is not None:
                self.postorder(n.right)
            
            print(n.item, end=' ')
    
    def levelorder(self, root):
        q = deque()
        q.append(root)
        
        while q:
            node = q.popleft()
            print(node.item, end=' ')
            
            if node.left is not None:
                q.append(node.left)
            
            if node.right is not None:
                q.append(node.right)
    
    def height(self, root):
        if root is None:
            return 0
        
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        
        return max(left_height, right_height) + 1

    def size(self, root):
        if root is None:
            return 0
        
        return self.size(root.left) + self.size(root.right) + 1

    def leaf_nodes(self, root):
        if root is None:
            return 0
        
        if root.left is None and root.right is None:
            return 1
        
        return self.leaf_nodes(root.left) + self.leaf_nodes(root.right)

    def copy_tree(self, n):
        if n is None:
            return None
        
        new_node = self.Node(n.item)
        new_node.left = self.copy_tree(n.left)
        new_node.right = self.copy_tree(n.right)
        
        return new_node
    
    def is_equal(self, n, m):
        if n is None and m is None:
            return True
        
        if n is None or m is None:
            return False
        
        return (n.item == m.item and
                self.is_equal(n.left, m.left) and
                self.is_equal(n.right, m.right))

if __name__ == "__main__":
    tree = BinaryTree()
    n1 = tree.Node(1)
    n2 = tree.Node(2)
    n3 = tree.Node(3)
    n4 = tree.Node(4)
    n5 = tree.Node(5)
    n6 = tree.Node(6)
    n7 = tree.Node(7)
    n8 = tree.Node(8)
    
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    n4.left = n8
    tree.root = n1
    
    print("Preorder traversal:")
    tree.preorder(tree.root)
    print("\n")
    
    print("Inorder traversal:")
    tree.inorder(tree.root)
    print("\n")
    
    print("Postorder traversal:")
    tree.postorder(tree.root)
    print("\n")
    
    print("Levelorder traversal:")
    tree.levelorder(tree.root)
    print("\n")
    
    print("Height of the tree:", tree.height(tree.root))
    print()
    
    print("Size of the tree:", tree.size(tree.root))
    print()
    
    print("Leaf size of the tree:", tree.leaf_nodes(tree.root))
    print()
    
    copy_tree = tree.copy_tree(tree.root)
    print("Is the copied tree equal to the original tree?", tree.is_equal(tree.root, copy_tree))
    print()