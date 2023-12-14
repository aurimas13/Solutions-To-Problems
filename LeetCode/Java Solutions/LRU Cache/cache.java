import java.util.LinkedHashMap;
import java.util.Map;

class LRUCache {
    private LinkedHashMap<Integer, Integer> cache;  // LinkedHashMap used to store the key-value pairs
    private int capacity;  // Maximum capacity of the cache

    public LRUCache(int capacity) {
        // Initialize the cache with the specified capacity and a load factor of 0.75
        // The last parameter "true" indicates that the access order should be maintained
        this.cache = new LinkedHashMap<>(capacity, 0.75f, true) {
            // Override removeEldestEntry to implement LRU eviction strategy
            protected boolean removeEldestEntry(Map.Entry<Integer, Integer> eldest) {
                // Return true if the size of the cache exceeds the capacity
                return size() > capacity;
            }
        };
        this.capacity = capacity;  // Set the maximum capacity of the cache
    }

    public int get(int key) {
        // Return the value associated with the given key, or -1 if not found
        return cache.getOrDefault(key, -1);
    }

    public void put(int key, int value) {
        // Add or update the key-value pair in the cache
        cache.put(key, value);
    }
}

public class Main {
    public static void main(String[] args) {
        LRUCache lruCache = new LRUCache(2);  // Create an instance of the LRUCache with capacity 2
        lruCache.put(1, 1);  // Add key-value pair (1, 1) to the cache
        lruCache.put(2, 2);  // Add key-value pair (2, 2) to the cache
        assert lruCache.get(1) == 1;  // Retrieve the value associated with key 1, should be 1
        lruCache.put(3, 3);  // Add key-value pair (3, 3) to the cache, evicting (2, 2) as it was the least recently used
        assert lruCache.get(2) == -1;  // Key 2 is not found in the cache, should return -1
        lruCache.put(4, 4);  // Add key-value pair (4, 4) to the cache, evicting (1, 1) as it was the least recently used
        assert lruCache.get(1) == -1;  // Key 1 is not found in the cache, should return -1
        assert lruCache.get(3) == 3;  // Retrieve the value associated with key 3, should be 3
        assert lruCache.get(4) == 4;  // Retrieve the value associated with key 4, should be 4
    }
}
