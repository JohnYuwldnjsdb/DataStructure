class LinearProbing:
    def __init__(self, size):
        self.M = size
        self.a = [None] * size
        self.d = [None] * size

    def hash(self, key):
        return key % self.M

    def put(self, key, data):
        initial_position = self.hash(key)
        i = initial_position
        j = 0
        
        while True:
            if self.a[i] == None:
                self.a[i] = key
                self.d[i] = data
                return
            
            if self.a[i] == key:
                self.d[i] = data
                return
            
            j += 1
            i = (initial_position + j) % self.M
            
            if i == initial_position:
                break
    
    def get(self, key):
        initial_position = self.hash(key)
        i = initial_position
        j = 0
        
        while self.a[i] != None:
            if self.a[i] == key:
                return self.d[i]
            
            j += 1
            i = (initial_position + j) % self.M
            
            if i == initial_position:
                break
        
        return None
    
    def print_table(self):
        for i in range(self.M):
            print(f"{i:<12}", end = "")
        print()
        
        for i in range(self.M):
            print(f"{str(self.a[i]):12}", end = "")
        print()
        
        for i in range(self.M):
            print(f"{str(self.d[i]):12}", end = "")
        print()

if __name__ == "__main__":
    t = LinearProbing(13)
    t.put(25, "grape")
    t.put(37, "apple")
    t.put(18, "banana")
    t.put(55, "cherry")
    t.put(22, "mango")
    t.put(35, "lime")
    t.put(50, "orange")
    t.put(63, "watermelon")
    print('탐색 결과:')
    print("50의 data:",t.get(50))
    print("63의 data:",t.get(63))
    print("해시 테이블:")
    t.print_table()