import java.util.TreeMap;
import java.util.HashMap;

class SnapshotArray {
    private HashMap<Integer, TreeMap<Integer, Integer>> map;
    private int snapId = 0;

    public SnapshotArray(int length) {
        map = new HashMap<>();
        for (int i = 0; i < length; i++) {
            map.put(i, new TreeMap<>());
            map.get(i).put(0, 0);
        }
    }

    /** Sets the value of an entry at the specified index for the given snapshot ID.
    * @param index the index of the entry
    * @param snapId the snapshot ID
    * @param val the value to set
    */

    public void set(int index, int val) {
        map.get(index).put(snapId, val);
    }
    
    /** Increments and returns the current snap ID.
    * @return the current snap ID
    */
    
    public int snap() {
        return snapId++;
    }
    
    /** Returns the value associated with the given snap_id key in the TreeMap at the given index
    * @param index the index of the TreeMap to search
    * @param snap_id the key to search for in the TreeMap
    * @return the value associated with the given snap_id key in the TreeMap at the given index
    */

    public int get(int index, int snap_id) {
        return map.get(index).floorEntry(snap_id).getValue();
    }
}

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * SnapshotArray obj = new SnapshotArray(length);
 * obj.set(index,val);
 * int param_2 = obj.snap();
 * int param_3 = obj.get(index,snap_id);
 */
