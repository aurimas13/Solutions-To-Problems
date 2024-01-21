import random

class RandomizedSet:
    def __init__(self):
        self.dict = {}  # Maps element to its index in the list
        self.list = []  # Dynamic array to store the elements

    def insert(self, val: int) -> bool:
        if val not in self.dict:
            self.dict[val] = len(self.list)  # Store index of val in the list
            self.list.append(val)  # Append val to the list
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.dict:
            # Swap the element with the last element
            last_element, idx_to_remove = self.list[-1], self.dict[val]
            self.list[idx_to_remove], self.dict[last_element] = last_element, idx_to_remove
            self.list.pop()  # Remove the last element
            del self.dict[val]  # Remove the element from the dictionary
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.list)  # Return a random element
