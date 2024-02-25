import java.util.*;

public class Solution {
    // Union-Find class for managing disjoint sets
    class UnionFind {
        private int[] parent;

        public UnionFind(int size) {
            parent = new int[size];
            for (int i = 0; i < size; i++) {
                parent[i] = i;
            }
        }

        public int find(int x) {
            if (parent[x] != x) {
                parent[x] = find(parent[x]);
            }
            return parent[x];
        }

        public void union(int x, int y) {
            parent[find(x)] = find(y);
        }
    }

    public boolean canTraverseAllPairs(int[] nums) {
        int n = nums.length;
        Map<Integer, List<Integer>> primeToIndices = new HashMap<>();
        UnionFind uf = new UnionFind(n);

        for (int i = 0; i < n; i++) {
            for (int factor : factorize(nums[i])) {
                primeToIndices.computeIfAbsent(factor, k -> new ArrayList<>()).add(i);
            }
        }

        for (List<Integer> indices : primeToIndices.values()) {
            for (int i = 1; i < indices.size(); i++) {
                uf.union(indices.get(0), indices.get(i));
            }
        }

        int root = uf.find(0);
        for (int i = 1; i < n; i++) {
            if (uf.find(i) != root) {
                return false;
            }
        }
        return true;
    }

    private List<Integer> factorize(int num) {
        Set<Integer> factors = new HashSet<>();
        for (int factor = 2; factor * factor <= num; factor++) {
            while (num % factor == 0) {
                factors.add(factor);
                num /= factor;
            }
        }
        if (num > 1) {
            factors.add(num);
        }
        return new ArrayList<>(factors);
    }
}
