from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
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


# # Checking in console
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.addTwoNumbers([2,4,3], [5,6,4])  #  "aabb" -> ['baab', 'abba']
    print(Solve)
