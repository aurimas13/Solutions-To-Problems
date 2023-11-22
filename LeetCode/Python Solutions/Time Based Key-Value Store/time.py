from collections import defaultdict

class TimeMap:
    def __init__(self):
        # Initialize a dictionary to store key-value pairs with timestamps
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Append the value and timestamp as a tuple to the key's list in the dictionary
        self.store[key].append((timestamp, value))

    def _binary_search(self, key, timestamp):
        left, right = 0, len(self.store[key]) - 1

        while left <= right:
            mid = (left + right) // 2

            if self.store[key][mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid - 1

        return right

    def get(self, key: str, timestamp: int) -> str:
        # If the key is not present in the store, return an empty string
        if key not in self.store:
            return ""

        # Use the custom _binary_search function to find the index of the highest timestamp less than or equal to the given timestamp
        index = self._binary_search(key, timestamp)
        
        # If index is -1, it means there's no value before the given timestamp
        if index == -1:
            return ""
        
        # If index >= 0, return the value at the found index
        return self.store[key][index][1]

if __name__ == '__main__':
    time_map = TimeMap()
    time_map.set("foo", "bar", 1)
    time_map.set("foo", "baz", 3)
    assert time_map.get("foo", 0) == ""
    assert time_map.get("foo", 1) == "bar"
    assert time_map.get("foo", 2) == "bar"
    assert time_map.get("foo", 3) == "baz"
    assert time_map.get("foo", 4) == "baz"