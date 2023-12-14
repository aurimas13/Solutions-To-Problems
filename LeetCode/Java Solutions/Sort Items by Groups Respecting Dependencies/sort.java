import java.util.*;

public class Solution {
    
    public int[] sortItems(int n, int m, int[] group, List<List<Integer>> beforeItems) {
        
        // Assign new groups for items without a group.
        for (int i = 0; i < n; i++) {
            if (group[i] == -1) {
                group[i] = m;
                m++; // Increase the group count
            }
        }
        
        // Create an adjacency list (dependency graph) for items
        List<Integer>[] itemGraph = new ArrayList[n];
        for (int i = 0; i < n; i++) itemGraph[i] = new ArrayList<>();
        
        // In-degree count for all items. Used for topological sort.
        int[] itemInDegree = new int[n];
        
        // Create an adjacency list (dependency graph) for groups
        List<Integer>[] groupGraph = new ArrayList[m];
        for (int i = 0; i < m; i++) groupGraph[i] = new ArrayList<>();
        
        // In-degree count for groups. Used for topological sort.
        int[] groupInDegree = new int[m];
        
        // Construct the graphs based on beforeItems list
        for (int i = 0; i < n; i++) {
            for (int preItem : beforeItems.get(i)) {
                itemGraph[preItem].add(i);
                itemInDegree[i]++;
                
                if (group[i] != group[preItem]) {
                    groupGraph[group[preItem]].add(group[i]);
                    groupInDegree[group[i]]++;
                }
            }
        }
        
        // Topological sort on items and groups
        List<Integer> itemOrder = topologicalSort(itemGraph, itemInDegree);
        List<Integer> groupOrder = topologicalSort(groupGraph, groupInDegree);
        
        // If we can't get a valid order, return []
        if (itemOrder.size() != n || groupOrder.size() != m) return new int[0];
        
        // Arrange items within each group in the sorted order
        Map<Integer, List<Integer>> groupToItems = new HashMap<>();
        for (int item : itemOrder) {
            groupToItems.putIfAbsent(group[item], new ArrayList<>());
            groupToItems.get(group[item]).add(item);
        }
        
        // Combine items from all groups in the order of sorted groups.
        int[] sortedItems = new int[n];
        int idx = 0;
        for (int groupId : groupOrder) {
            if (groupToItems.containsKey(groupId)) {  // Check if group has items
                for (int item : groupToItems.get(groupId)) {
                    sortedItems[idx++] = item;
                }
            }
        }
        
        return sortedItems;
    }
    
    private List<Integer> topologicalSort(List<Integer>[] graph, int[] indegree) {
        List<Integer> sortedOrder = new ArrayList<>();
        Queue<Integer> zeroInDegree = new LinkedList<>();
        
        for (int i = 0; i < indegree.length; i++) {
            if (indegree[i] == 0) zeroInDegree.add(i);
        }
        
        while (!zeroInDegree.isEmpty()) {
            int node = zeroInDegree.poll();
            sortedOrder.add(node);
            for (int neighbor : graph[node]) {
                indegree[neighbor]--;
                if (indegree[neighbor] == 0) zeroInDegree.add(neighbor);
            }
        }
        
        return sortedOrder;
    }
}
