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
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;
        while (curr != null) {
            ListNode nextTemp = curr.next; // Save next node
            curr.next = prev; // Reverse current node's pointer
            prev = curr; // Move prev one step forward
            curr = nextTemp; // Move curr one step forward
        }
        return prev; // Prev will be the new head after the loop
    }
}