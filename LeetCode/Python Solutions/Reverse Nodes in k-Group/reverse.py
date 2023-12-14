class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 1:
            return head

        # Calculate the length of the list
        length, current = 0, head
        while current:
            length += 1
            current = current.next

        dummy = ListNode(next=head)
        prev_node = dummy

        # Reverse k-group
        while length >= k:
            start_node, end_node = prev_node.next, prev_node
            for _ in range(k + 1):
                end_node = end_node.next

            next_group_start = start_node.next
            for _ in range(k - 1):
                tmp = start_node.next
                start_node.next = tmp.next
                tmp.next = prev_node.next
                prev_node.next = tmp

            start_node.next = end_node

            prev_node = start_node
            length -= k

        return dummy.next


def create_linked_list(values):
    dummy = ListNode()
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next


def linked_list_to_list(head):
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    return values


if __name__ == '__main__':
    solution = Solution()

    test_cases = [
        ([1, 2, 3, 4, 5], 2, [2, 1, 4, 3, 5]),
        ([1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5]),
        ([1, 2, 3, 4, 5], 1, [1, 2, 3, 4, 5]),
        ([], 3, [])
    ]

    for values, k, expected in test_cases:
        head = create_linked_list(values)
        result = solution.reverseKGroup(head, k)
        result_values = linked_list_to_list(result)
        assert result_values == expected, f"For {values}, k={k}, expected {expected} but got {result_values}"

    print("All tests passed!")
