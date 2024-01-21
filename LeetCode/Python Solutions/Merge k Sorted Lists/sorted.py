import heapq
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Create a dummy head node for the merged list
        dummy_head = ListNode()
        current = dummy_head

        # Create a min-heap to store the smallest elements from each list
        min_heap = [(node.val, index) for index, node in enumerate(lists) if node]
        heapq.heapify(min_heap)

        # Continue merging elements until the min-heap is empty
        while min_heap:
            # Pop the smallest element and its index from the min-heap
            value, index = heapq.heappop(min_heap)

            # Add the smallest element to the merged list
            current.next = ListNode(value)
            current = current.next

            # Move the pointer in the original list and push the next element to the min-heap
            lists[index] = lists[index].next
            if lists[index]:
                heapq.heappush(min_heap, (lists[index].val, index))

        return dummy_head.next


if __name__ == '__main__':
    def list_to_linked_list(lst):
        dummy_head = ListNode()
        current = dummy_head
        for val in lst:
            current.next = ListNode(val)
            current = current.next
        return dummy_head.next

    def linked_list_to_list(head):
        lst = []
        current = head
        while current:
            lst.append(current.val)
            current = current.next
        return lst

    s = Solution()

    test_cases = [
        ([], []),
        ([
            [1, 4, 5],
            [1, 3, 4],
            [2, 6]
        ], [1, 1, 2, 3, 4, 4, 5, 6]),
    ]

    for test_input, expected_output in test_cases:
        input_lists = [list_to_linked_list(lst) for lst in test_input]
        merged_head = s.mergeKLists(input_lists)
        assert linked_list_to_list(merged_head) == expected_output
