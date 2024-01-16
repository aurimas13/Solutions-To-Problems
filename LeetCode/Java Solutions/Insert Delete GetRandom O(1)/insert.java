import java.util.*;

public class RandomizedSet {
    private Map<Integer, Integer> map;  // Maps element to its index
    private List<Integer> list;  // Dynamic array to store elements
    private Random rand = new Random();

    public RandomizedSet() {
        map = new HashMap<>();
        list = new ArrayList<>();
    }

    public boolean insert(int val) {
        if (!map.containsKey(val)) {
            map.put(val, list.size());  // Store index of val
            list.add(val);  // Append val to the list
            return true;
        }
        return false;
    }

    public boolean remove(int val) {
        if (map.containsKey(val)) {
            int lastElement = list.get(list.size() - 1);
            int idxToRemove = map.get(val);

            // Swap with the last element
            list.set(idxToRemove, lastElement);
            map.put(lastElement, idxToRemove);

            list.remove(list.size() - 1); // Remove the last element
            map.remove(val); // Remove the element from the map
            return true;
            }
        return false;
        }

    public int getRandom() {
        return list.get(rand.nextInt(list.size()));  // Return a random element
    }
}