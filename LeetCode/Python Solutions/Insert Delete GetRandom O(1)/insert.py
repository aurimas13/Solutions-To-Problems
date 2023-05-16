import random


class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.list = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.dict:
            self.dict[val] = len(self.list)
            self.list.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.dict:
            last, idx = self.list[-1], self.dict[val]
            self.list[idx], self.dict[last] = last, idx
            self.list.pop()
            del self.dict[val]
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.list)


if __name__ == "__main__":
    # Your RandomizedSet object will be instantiated and called as such:
    obj = RandomizedSet()
    assert obj.insert(1) == True
    assert obj.remove(2) == False
    assert obj.insert(2) == True
    assert obj.getRandom() in [1, 2]
    assert obj.remove(1) == True
    assert obj.insert(2) == False
    assert obj.getRandom() == 2
