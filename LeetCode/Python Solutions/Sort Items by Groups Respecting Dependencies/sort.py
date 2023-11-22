from collections import defaultdict
from typing import List, Dict

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        # Assign new groups for items without a group.
        # Start new group ids from m as [0 to m-1] already used.
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1  # increase the group count
        
        # Create an adjacency list (dependency graph) for items
        item_graph = defaultdict(list)
        # In-degree count for all items. Used for topological sort.
        item_indegree = [0] * n
        # Create an adjacency list (dependency graph) for groups
        group_graph = defaultdict(list)
        # In-degree count for groups. Used for topological sort.
        group_indegree = [0] * m
        
        # Construct the graphs based on beforeItems list
        for i in range(n):
            for pre_item in beforeItems[i]:
                item_graph[pre_item].append(i)
                item_indegree[i] += 1
                
                # If the two items 'i' and 'pre_item' are from different groups, 
                # add an edge between these groups.
                if group[i] != group[pre_item]:
                    group_graph[group[pre_item]].append(group[i])
                    group_indegree[group[i]] += 1
        
        # Topological sort on items and groups
        item_order = self.topological_sort(item_graph, item_indegree)
        group_order = self.topological_sort(group_graph, group_indegree)
        
        # If we can't get a valid order, return []
        if not item_order or not group_order:
            return []
        
        # Arrange items within each group in the sorted order
        group_to_items = defaultdict(list)
        for item in item_order:
            group_to_items[group[item]].append(item)
        
        # Combine items from all groups in the order of sorted groups.
        sorted_items = []
        for group_id in group_order:
            sorted_items.extend(group_to_items[group_id])
        
        return sorted_items
    
    def topological_sort(self, graph: Dict[int, List[int]], indegree: List[int]) -> List[int]:
        # Initialize a result list and a stack to keep nodes with 0 in-degree
        sorted_order = []
        zero_indegree = [i for i, deg in enumerate(indegree) if deg == 0]
        
        # While we have nodes with 0 in-degree, process them
        while zero_indegree:
            node = zero_indegree.pop()  # get a node with 0 in-degree
            sorted_order.append(node)   # add to result list
            # Decrease in-degree for all neighbors
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                # If neighbor becomes 0 in-degree, add to stack
                if indegree[neighbor] == 0:
                    zero_indegree.append(neighbor)
        
        # Return sorted order if we have processed all nodes; otherwise, return []
        return sorted_order if len(sorted_order) == len(graph) else []
