# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
#     def hasCycle(self, head: ListNode) -> bool:
#         if head is None:
#             return False
#         slow = head
#         fast = head.next
#         while slow != fast:
#             if fast is None or fast.next is None:
#                 return False
#             slow = slow.next
#             fast = fast.next.next
#         return True


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        nodes_seen = set()
        while head is not None:
            if head in nodes_seen:
                return True
            nodes_seen.add(head)
            head = head.next
        return False


if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.hasCycle(ListNode([3,2,0,-4])) #  ListNode([3,2,0,-4]) -> False
    print(Solve)
