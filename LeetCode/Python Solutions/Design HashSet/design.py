class MyHashSet:
    def __init__(self):
        self.hashSet = [False] * 1000001

    def add(self, key: int) -> None:
        self.hashSet[key] = True

    def remove(self, key: int) -> None:
        self.hashSet[key] = False

    def contains(self, key: int) -> bool:
        return self.hashSet[key]


if __name__ == "__main__":
    # Create a HashSet object
    hashSet = MyHashSet()

    # Add elements to the hash set
    hashSet.add(1)
    hashSet.add(2)
    hashSet.add(3)

    # Remove an element from the hash set
    hashSet.remove(2)

    # Check if the hash set contains a specific element
    contains = hashSet.contains(3)
    print(f"Contains 3: {contains}")
