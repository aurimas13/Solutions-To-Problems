import java.util.*;

public class Solution {
    List<Integer>[] tree;
    int[] count;
    int[] answer;

    public int[] sumOfDistancesInTree(int n, int[][] edges) {
        tree = new List[n];
        count = new int[n];
        answer = new int[n];

        // Initialize tree adjacency list
        for (int i = 0; i < n; i++) {
            tree[i] = new ArrayList<>();
        }
        for (int[] edge : edges) {
            tree[edge[0]].add(edge[1]);
            tree[edge[1]].add(edge[0]);
        }

        // First pass: post-order DFS
        dfsPostOrder(0, -1);
        // Second pass: pre-order DFS
        dfsPreOrder(0, -1);

        return answer;
    }

    private void dfsPostOrder(int node, int parent) {
        count[node] = 1;  // Start count with itself
        for (int child : tree[node]) {
            if (child != parent) {
                dfsPostOrder(child, node);
                count[node] += count[child];
                answer[node] += answer[child] + count[child];
            }
        }
    }

    private void dfsPreOrder(int node, int parent) {
        // Root node's answer already computed in post-order
        for (int child : tree[node]) {
            if (child != parent) {
                answer[child] = answer[node] - count[child] + (tree.length - count[child]);
                dfsPreOrder(child, node);
            }
        }
    }
}
