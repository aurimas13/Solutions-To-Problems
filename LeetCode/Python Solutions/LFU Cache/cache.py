from collections import defaultdict, OrderedDict

class LFUCache:

    def __init__(self, capacity: int):
        # Initialize the cache, frequencies, and minimum frequency
        self.capacity = capacity
        self.cache = {}
        self.frequencies = defaultdict(OrderedDict)
        self.min_freq = 1

    def _update(self, key: int):
        # Update the frequency of the key and its position in the frequencies dict
        freq = self.cache[key][1]
        self.frequencies[freq].pop(key)
        
        if not self.frequencies[freq]:
            self.frequencies.pop(freq)
            if self.min_freq == freq:
                self.min_freq += 1
        
        self.cache[key] = (self.cache[key][0], freq + 1)
        self.frequencies[freq + 1][key] = None

    def get(self, key: int) -> int:
        # If the key is not in the cache, return -1
        if key not in self.cache:
            return -1

        # Update the frequency and position of the key
        self._update(key)

        # Return the value associated with the key
        return self.cache[key][0]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.cache:
            self._update(key)
            self.cache[key] = (value, self.cache[key][1])
        else:
            if len(self.cache) == self.capacity:
                least_frequent_key, _ = self.frequencies[self.min_freq].popitem(last=False)
                self.cache.pop(least_frequent_key)
            
            self.cache[key] = (value, 1)
            self.frequencies[1][key] = None
            self.min_freq = 1


# Tests:
if __name__ == '__main__':
    lfu_cache = LFUCache(2)
    lfu_cache.put(1, 1)
    lfu_cache.put(2, 2)
    assert lfu_cache.get(1) == 1
    lfu_cache.put(3, 3)
    assert lfu_cache.get(2) == -1
    assert lfu_cache.get(3) == 3
    lfu_cache.put(4, 4)
    assert lfu_cache.get(1) == -1
    assert lfu_cache.get(3) == 3
    assert lfu_cache.get(4) == 4