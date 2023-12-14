# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: if the list is empty or has only one element, return the list
        if not head or not head.next:
            return head

        # Store the second element of the list
        second_node = head.next

        # Recursively swap the pairs in the remaining list
        head.next = self.swapPairs(second_node.next)

        # Swap the first two elements
        second_node.next = head

        # Return the new head of the list
        return second_node


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
        ([1], [1]),
        ([1, 2], [2, 1]),
        ([1, 2, 3], [2, 1, 3]),
        ([1, 2, 3, 4], [2, 1, 4, 3]),
    ]

    for test_input, expected_output in test_cases:
        input_head = list_to_linked_list(test_input)
        swapped_head = s.swapPairs(input_head)
        assert linked_list_to_list(swapped_head) == expected_output
