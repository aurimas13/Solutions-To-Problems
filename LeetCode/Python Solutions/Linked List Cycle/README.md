Problem description of "Linked List Cycle" can be found [here](https://leetcode.com/problems/linked-list-cycle/) while the solution is found [here]().

**Explanation**:

1. The slow pointer moves one step at a time while the fast pointer moves two steps.
2. If the linked list has a cycle, then the fast pointer will eventually meet the slow pointer.
3. If the fast pointer reaches the end of the list (either it becomes null or its next node is null), then the list does not have a cycle.

**Implementation**:

Imagine a racing track. If the track is a closed circuit (has a cycle), a faster runner (the hare) will eventually lap the slower runner (the tortoise). On the other hand, if the track is a straight path with a finish line (no cycle), the faster runner will just reach the end without ever meeting the slower runner again.
