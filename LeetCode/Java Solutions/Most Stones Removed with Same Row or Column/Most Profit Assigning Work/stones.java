class Solution {
    class UnionFind {
        Map<Integer, Integer> parent = new HashMap<>();
        
        int find(int x) {
            if (!parent.containsKey(x)) {
                parent.put(x, x);
            } else if (parent.get(x) != x) {
                parent.put(x, find(parent.get(x)));
            }
            return parent.get(x);
        }
        
        void union(int x, int y) {
            int rootX = find(x);
            int rootY = find(y);
            if (rootX != rootY) {
                parent.put(rootX, rootY);
            }
        }
    }
    
    public int removeStones(int[][] stones) {
        UnionFind uf = new UnionFind();
        for (int[] stone : stones) {
            uf.union(stone[0], stone[1] + 10001);  // offset y to avoid collision with x
        }
        
        Set<Integer> groups = new HashSet<>();
        for (int[] stone : stones) {
            groups.add(uf.find(stone[0]));
            groups.add(uf.find(stone[1] + 10001));
        }
        
        return stones.length - groups.size();
    }
}