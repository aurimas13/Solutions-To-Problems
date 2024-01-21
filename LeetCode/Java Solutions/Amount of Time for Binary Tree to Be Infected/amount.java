class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    public int amountOfTime(TreeNode root, int start) {
        // Convert tree to graph
        Map<Integer, List<Integer>> graph = new HashMap<>();
        buildGraph(root, null, graph);

        // BFS to simulate infection spread
        Set<Integer> visited = new HashSet<>();
        Queue<Pair<Integer, Integer>> queue = new LinkedList<>();
        queue.offer(new Pair<>(start, 0));
        int maxTime = 0;

        while (!queue.isEmpty()) {
            Pair<Integer, Integer> pair = queue.poll();
            int node = pair.getKey();
            int time = pair.getValue();

            if (!visited.contains(node)) {
                visited.add(node);
                maxTime = Math.max(maxTime, time);
                for (int neighbor : graph.getOrDefault(node, new ArrayList<>())) {
                    if (!visited.contains(neighbor)) {
                        queue.offer(new Pair<>(neighbor, time + 1));
                    }
                }
            }
        }

        return maxTime;
    }

    private void buildGraph(TreeNode node, TreeNode parent, Map<Integer, List<Integer>> graph) {
        if (node != null) {
            if (!graph.containsKey(node.val)) {
                graph.put(node.val, new ArrayList<>());
            }
            if (parent != null) {
                graph.get(node.val).add(parent.val);
                graph.get(parent.val).add(node.val);
            }
            buildGraph(node.left, node, graph);
            buildGraph(node.right, node, graph);
        }
    }
}
