from collections import deque

class Node:
    def __init__(self, key, value, left = None, right = None):
        self.key = key
        self.item = value
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None
    
    def get(self, key):
        return self.get_item(self.root, key)
    
    def get_item(self, n, k):
        if n == None:
            return None
        if n.key > k:
            return self.get_item(n.left, k)
        elif n.key < k:
            return self.get_item(n.right, k)
        else:
            return n.item
    
    def put(self, key, value):
        self.root = self.put_item(self.root, key, value)

    def put_item(self, n, key, value):
        if n == None:
            return Node(key, value)
        if n.key > key:
            n.left = self.put_item(n.left, key, value)
        elif n.key < key:
            n.right = self.put_item(n.right, key, value)
        else:
            n.value = value
        return n
    
    def min(self):
        if self.root == None:
            return None
        return self.get_min(self.root)
    
    def get_min(self, n):
        if n.left == None:
            return n
        return self.get_min(n.left)
    
    def delete_min(self):
        if self.root == None:
            print("Deletion attempted on a blank tree")
            return
        self.del_min(self.root)
    
    def del_min(self, n):
        if n.left == None:
            return n.right
        n.left = self.del_min(n.left)
        return n
    
    def delete(self, k):
        self.del_node(self.root, k)
    
    def del_node(self, n, k):
        if n == None:
            return None
        if n.key > k:
            n.left = self.del_node(n.left, k)
        elif n.key < k:
            n.right = self.del_node(n.right, k)
        else:
            if n.right == None:
                return n.left
            if n.left == None:
                return n.right
            target = n
            n = self.get_min(target.right) # 오른쪽 자식 최댓값
            n.right = self.del_min(target.right) # target의 오른쪽 자식을 n의 오른쪽 자식으로 설정 -> 두 트리 간섭 X
            n.left = target.left # target의 왼쪽 자식을 n의 왼쪽 자식으로 설정
        return n
    
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

if __name__ == "__main__":
    t = BST() # 이진탐색트리 객체 t 생성
    t.put(500, 'apple')
    t.put(600, 'banana')
    t.put(200, 'melon')
    t.put(100, 'orange')
    t.put(400, 'lime')
    t.put(250, 'kiwi')
    t.put(150, 'grape')
    t.put(800, 'peach')
    t.put(700, 'cherry')
    t.put(50,  'pear')
    t.put(350, 'lemon')
    t.put(10,  'plum')
    print('전위순회:\t', end='')
    t.preorder(t.root)
    print('\n중위순회:\t', end='')
    t.inorder(t.root)
    print('\n250: ',t.get(250))
    t.delete(200)
    print('200 삭제 후:')
    print('전위순회:\t', end='')
    t.preorder(t.root)
    print('\n중위순회:\t', end='')
    t.inorder(t.root)