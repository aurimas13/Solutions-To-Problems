import java.util.HashSet;

class MyHashSet {
    private HashSet<Integer> set;

    public MyHashSet() {
        set = new HashSet<>();
    }

    public void add(int key) {
        set.add(key);
    }

    public void remove(int key) {
        set.remove(key);
    }

    public boolean contains(int key) {
        return set.contains(key);
    }
}

public class Main {
    public static void main(String[] args) {
        MyHashSet hashSet = new MyHashSet();

        // Add elements to the hash set
        hashSet.add(1);
        hashSet.add(2);
        hashSet.add(3);

        // Remove an element from the hash set
        hashSet.remove(2);

        // Check if the hash set contains a specific element
        boolean contains = hashSet.contains(3);
        System.out.println("Contains 3: " + contains);
    }
}
