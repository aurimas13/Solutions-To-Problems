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
   public void reorderList(ListNode head) {
       if (head == null || head.next == null) return;
       
       // Find the middle of the list
       ListNode slow = head, fast = head;
       while (fast != null && fast.next != null) {
           slow = slow.next;
           fast = fast.next.next;
       }
       
       // Reverse the second half of the list
       ListNode prev = null, curr = slow.next;
       while (curr != null) {
           ListNode nextTemp = curr.next;
           curr.next = prev;
           prev = curr;
           curr = nextTemp;
       }
       slow.next = null; // Split the list into two parts
       
       // Merge two halves
       ListNode first = head, second = prev;
       while (second != null) {
           ListNode temp1 = first.next, temp2 = second.next;
           first.next = second;
           second.next = temp1;
           first = temp1;
           second = temp2;
       }
   }
}
