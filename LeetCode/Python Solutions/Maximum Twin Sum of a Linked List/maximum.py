class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


class Solution:
    def pairSum(self, head: ListNode) -> int:
        """
        Given the head of a linked list with even length, return the maximum
        twin sum of the linked list.
        """
        # store values of the nodes in a list
        values = []
        while head:
            values.append(head.val)
            head = head.next

        # calculate twin sums for the first half of the list
        twin_sums = [values[i] + values[-(i + 1)] for i in range(len(values) // 2)]

        # return the maximum twin sum
        return max(twin_sums)

# Tests:
if __name__ == "__main__":
    # Test case 1
    node1 = ListNode(1)
    node2 = ListNode(2, node1)
    node3 = ListNode(4, node2)
    head = ListNode(5, node3)

    sol = Solution()
    result = sol.pairSum(head)
    print(f"Maximum Twin Sum: {result}")  # Output: 6

    # Test case 2
    node1 = ListNode(3)
    node2 = ListNode(2, node1)
    node3 = ListNode(2, node2)
    head = ListNode(4, node3)

    result = sol.pairSum(head)
    print(f"Maximum Twin Sum: {result}")  # Output: 7

    # Test case 3
    node1 = ListNode(100000)
    head = ListNode(1, node1)

    result = sol.pairSum(head)
    print(f"Maximum Twin Sum: {result}")  # Output: 100001