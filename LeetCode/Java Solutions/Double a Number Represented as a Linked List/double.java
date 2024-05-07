/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    private ListNode reverse(ListNode head) {
        ListNode prev = null;
        ListNode current = head;
        while (current != null) {
            ListNode next = current.next;
            current.next = prev;
            prev = current;
            current = next;
        }
        return prev;
    }
    
    public ListNode doubleIt(ListNode head) {
        if (head == null) {
            return null;
        }
        
        // Reverse the list to start processing from the least significant digit
        head = reverse(head);
        
        ListNode current = head;
        int carry = 0;
        while (current != null) {
            int doubledValue = current.val * 2 + carry;
            current.val = doubledValue % 10;
            carry = doubledValue / 10;
            if (current.next == null && carry > 0) {
                current.next = new ListNode(carry);
                break;
            }
            current = current.next;
        }
        
        // Reverse the list to restore the original order
        return reverse(head);
    }
}