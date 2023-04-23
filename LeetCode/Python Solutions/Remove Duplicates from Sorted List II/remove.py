# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: 'Optional[ListNode]') -> 'Optional[ListNode]':
        # Create a dummy node and set its next pointer to head.
        dummy = ListNode(0, head)
        prev = dummy

        while head:
            # Check if head has duplicates.
            if head.next and head.val == head.next.val:
                # Skip all the duplicates.
                while head.next and head.val == head.next.val:
                    head = head.next
                prev.next = head.next
            else:
                prev = prev.next
            head = head.next

        return dummy.next


def list_to_linked_list(lst: 'List[int]') -> 'Optional[ListNode]':
    dummy = ListNode(0)
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


def linked_list_to_list(head: 'Optional[ListNode]') -> 'List[int]':
    lst = []
    while head:
        lst.append(head.val)
        head = head.next
    return lst


if __name__ == "__main__":
    s = Solution()

    # Test cases
    test_cases = [
        ({"head": [1, 2, 3, 3, 4, 4, 5]}, [1, 2, 5]),
        ({"head": [1, 1, 1, 2, 3]}, [2, 3]),
        ({"head": []}, []),
        ({"head": [1, 1]}, []),
    ]

    for i, (test_input, expected_output) in enumerate(test_cases):
        head = list_to_linked_list(test_input["head"])
        result_head = s.deleteDuplicates(head)
        result = linked_list_to_list(result_head)
        assert result == expected_output, f"Test case {i} failed: expected {expected_output}, got {result}"
        print(f"Test case {i} succeeded")
