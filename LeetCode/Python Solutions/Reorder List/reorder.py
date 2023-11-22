from typing import Optional


class ListNode:
   def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
   def reorderList(self, head: Optional[ListNode]) -> None:
      """
      Do not return anything, modify head in-place instead.
      """
      curr = head
      nodes = []
      while curr:
         nodes.append(curr)
         curr = curr.next

      l, r = 0, len(nodes) - 1
      while l < r:
         nodes[l].next, nodes[r].next = (
            nodes[r],
            nodes[l].next,
         )

         l += 1
         r -= 1

      nodes[l].next = None


# Test:
if __name__ == '__main__':
    val = ListNode(1)
    val.next = ListNode(2)
    val.next.next = ListNode(3)
    val.next.next.next = ListNode(4)
    val.next.next.next.next = ListNode(5)
    Instant = Solution()
    Instant.reorderList(val)  # head = [1,2,3,4,5] -> [1,5,2,4,3]

    # Print reordered list
    curr = val
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
