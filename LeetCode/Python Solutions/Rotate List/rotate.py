class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # Base case: if the list is empty or has only one element, no rotation is needed
        if not head or not head.next:
            return head
        
        # Calculate the length of the list and initialize a pointer to the head
        length = 1
        current = head
        while current.next:
            length += 1
            current = current.next

        # Calculate the effective number of rotations
        k %= length

        # If no rotation is needed, return the original head
        if k == 0:
            return head

        # Find the new head after rotation
        new_tail_index = length - k - 1
        new_tail = head
        for _ in range(new_tail_index):
            new_tail = new_tail.next

        # Update the new head and tail
        new_head = new_tail.next
        new_tail.next = None
        current.next = head

        return new_head


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
        ([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3]),
        ([0, 1, 2], 4, [2, 0, 1]),
        ([1, 2], 2, [1, 2]),
        ([], 3, [])
    ]

    for values, k, expected in test_cases:
        head = create_linked_list(values)
        result = solution.rotateRight(head, k)
        result_values = linked_list_to_list(result)
        assert result_values == expected, f"For {values}, k={k}, expected {expected} but got {result_values}"

    print("All tests passed!")
