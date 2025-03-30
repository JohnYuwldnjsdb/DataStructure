class Clist:
    class _Node:
        def __init__(self, item, next):
            self.item = item
            self.next = next
    
    def __init__(self):
        self.last = None
        self.size = 0
    
    def is_empty(self): return self.size == 0
    def get_size(self): return self.size
    
    def insert(self, item):
        n = self._Node(item, None)
        if self.is_empty():
            n.next = n
            self.last = n
        else:
            n.next = self.last.next
            self.last.next = n
        self.size += 1
    
    def first(self): # return the most recently inserted item
        if self.is_empty(): 
            raise EmptyError('Underflow')
        
        return self.last.next.item

    def delete(self): # remove the most recently inserted item
        if self.is_empty(): 
            raise EmptyError('Underflow')
        
        first_item = self.first()
        self.last.next = self.last.next.next
        self.size -= 1
        
        if self.is_empty():
            self.last = None
        
        return first_item

    def print_list(self):
        if self.is_empty():
            print('Circular linked list is empty')
        else:
            p = self.last.next
            while True:
                print(p.item, end=' ')
                p = p.next
                if p == self.last.next:
                    break
            print()

class EmptyError(Exception):
    pass

if __name__ == '__main__':
    c = Clist()
    c.insert(10)
    c.insert(20)
    c.insert(30)
    c.print_list()
    print('First item:', c.first())
    c.delete()
    c.print_list()
    c.delete()
    c.print_list()
    c.delete()
    c.print_list()