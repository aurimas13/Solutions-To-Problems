# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: 'Optional[ListNode]', k: int) -> 'Optional[ListNode]':
        # Initialize variables
        node = head
        for _ in range(k - 1):
            # Traverse the linked list until the kth node
            node = node.next

        # Save reference to the kth node
        kth_node_from_start = node

        # Initialize a new pointer at the head
        kth_node_from_end = head

        # Traverse the rest of the linked list
        while node.next:
            node = node.next
            kth_node_from_end = kth_node_from_end.next

        # Swap the values of the kth node from start and end
        kth_node_from_start.val, kth_node_from_end.val = kth_node_from_end.val, kth_node_from_start.val

        return head


# Test cases
if __name__ == "__main__":
    node4 = ListNode(4)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)

    solution = Solution()

    result = solution.swapNodes(node1, 2)

    # Print the linked list after swapping
    while result:
        print(result.val)
        result = result.next
