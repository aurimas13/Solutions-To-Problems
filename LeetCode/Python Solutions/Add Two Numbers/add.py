# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = ListNode((l1.val + l2.val) % 10)
        carry = (l1.val + l2.val) // 10
        node = root
        while l1.next or l2.next:
            s = (l1.next.val if l1.next else 0) + (l2.next.val if l2.next else 0) + carry
            node.next = ListNode(s % 10)
            if l1.next:
                l1 = l1.next
            if l2.next:
                l2 = l2.next
            node = node.next
            carry = s // 10
        if carry:
            node.next = ListNode(carry)
        return root


def create_linked_list(lst):
    dummy = ListNode(0)
    ptr = dummy
    for num in lst:
        ptr.next = ListNode(num)
        ptr = ptr.next
    return dummy.next


# Tests:
if __name__ == '__main__':
    Instant = Solution()
    list1 = create_linked_list([2, 4, 3])
    list2 = create_linked_list([5, 6, 4])
    Solve = Instant.addTwoNumbers(list1, list2)

    # To print the result, you may want to convert it back to a list
    result = []
    while Solve:
        result.append(Solve.val)
        Solve = Solve.next

    print(result)  # Expected: [7, 0, 8]
