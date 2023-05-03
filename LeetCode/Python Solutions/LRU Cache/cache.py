from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        # Initialize the OrderedDict and set the capacity
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        # If the key is not in the cache, return -1
        if key not in self.cache:
            return -1
        
        # Move the key-value pair to the end of the cache to mark it as recently used
        self.cache.move_to_end(key)
        
        # Return the value associated with the key
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        # If the key is already in the cache, move it to the end to mark it as recently used
        if key in self.cache:
            self.cache.move_to_end(key)

        # Insert the key-value pair into the cache
        self.cache[key] = value

        # If the cache has exceeded its capacity, remove the least recently used key-value pair
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

if __name__ == '__main__':
    lru_cache = LRUCache(2)
    lru_cache.put(1, 1)
    lru_cache.put(2, 2)
    assert lru_cache.get(1) == 1
    lru_cache.put(3, 3)
    assert lru_cache.get(2) == -1
    lru_cache.put(4, 4)
    assert lru_cache.get(1) == -1
    assert lru_cache.get(3) == 3
    assert lru_cache.get(4) == 4