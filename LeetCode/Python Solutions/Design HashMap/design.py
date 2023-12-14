class MyHashMap:

    def __init__(self):
        # For simplicity, we're using a large prime number as the array size
        # to reduce the chances of collisions.
        self.size = 10007
        self.data = [[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        index = key % self.size
        found = False
        for i, (k, v) in enumerate(self.data[index]):
            if k == key:
                self.data[index][i] = (key, value)
                found = True
                break
        if not found:
            self.data[index].append((key, value))

    def get(self, key: int) -> int:
        index = key % self.size
        for k, v in self.data[index]:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        index = key % self.size
        self.data[index] = [(k, v) for k, v in self.data[index] if k != key]

