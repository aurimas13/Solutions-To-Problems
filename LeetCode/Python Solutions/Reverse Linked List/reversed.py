# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        return prev

# if __name__ == '__main__':
#     Instant = Solution()
#     Solve = Instant.reverseList(ListNode([1,2,3,4,5]))
#     print(Solve)
