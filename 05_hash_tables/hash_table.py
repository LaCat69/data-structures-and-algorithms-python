class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.count = 0
    
    def _hash(self, key):
        return hash(key) % self.size
    
    def resize(self):
        old_table = self.table
        self.size *= 2
        self.table = [[] for _ in range(self.size)]
        self.count = 0
        for bucket in old_table:
            for k, v in bucket:
                self.put(k, v)
    
    def put(self, key, value):
        refactor = self.count / self.size
        if refactor > 0.7:
            self.resize()
        index = self._hash(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self.count += 1
    
    def get(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                return v
        return None
    
    def delete(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.count -= 1
                return v
        return None

ht = HashTable()

ht.put("user1@gmail.com", "pass123")
ht.put("user2@gmail.com", "qwerty")
ht.put("user3@gmail.com", "123456")

for i in range(1, 4):
    print(ht.get('user' + str(i) + '@gmail.com'))

for i in range(1, 4):
    print(ht.delete("user" + str(i) + "@gmail.com"))

for i in range(1, 4):
    print(ht.get('user' + str(i) + '@gmail.com'))

print(ht.size)
ht.put("user1@gmail.com", "pass123")
ht.put("user2@gmail.com", "qwerty")
ht.put("user3@gmail.com", "123456")
ht.put("user4@gmail.com", "6666")
ht.put("user5@gmail.com", "5555")
ht.put("user6@gmail.com", "4444")
ht.put("user7@gmail.com", "3333")
ht.put("user8@gmail.com", "2222")
ht.put("user9@gmail.com", "1111")
print(ht.size)

for i in range(1, 10):
    print(ht.get('user' + str(i) + '@gmail.com'))