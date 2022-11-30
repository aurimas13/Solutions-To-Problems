class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        new = ListNode()
        new.next = head

        curr = head
        prev = new
        last_end = new
        is_valid = True

        while curr:

            counter = 1
            checker = curr

            while counter < k:
                checker = checker.next
                if checker is None:
                    is_valid = False
                    break
                counter += 1

            if not is_valid:
                break

            counter = 0

            while counter < k:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                counter += 1

            swap_end = last_end.next
            last_end.next = prev
            swap_end.next = curr
            last_end = swap_end

        return new.next
