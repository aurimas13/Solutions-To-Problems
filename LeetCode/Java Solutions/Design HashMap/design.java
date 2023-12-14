import java.util.LinkedList;

class MyHashMap {
    private final int size = 10007;
    private LinkedList<Pair>[] data;

    // Helper class to store key-value pairs
    private class Pair {
        int key;
        int value;
        Pair(int key, int value) {
            this.key = key;
            this.value = value;
        }
    }

    public MyHashMap() {
        data = new LinkedList[size];
        for (int i = 0; i < size; i++) {
            data[i] = new LinkedList<>();
        }
    }

    public void put(int key, int value) {
        int index = key % size;
        boolean found = false;
        for (Pair pair : data[index]) {
            if (pair.key == key) {
                pair.value = value;
                found = true;
                break;
            }
        }
        if (!found) {
            data[index].add(new Pair(key, value));
        }
    }

    public int get(int key) {
        int index = key % size;
        for (Pair pair : data[index]) {
            if (pair.key == key) {
                return pair.value;
            }
        }
        return -1;
    }

    public void remove(int key) {
        int index = key % size;
        data[index].removeIf(pair -> pair.key == key);
    }
}
