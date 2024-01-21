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
    public ListNode[] splitListToParts(ListNode head, int k) {
        // Step 1: Find the length of the linked list
        int length = 0;
        ListNode current = head;
        while (current != null) {
            length++;
            current = current.next;
        }
        
        // Step 2: Calculate the size of each part
        int size = length / k;
        int remainder = length % k;
        
        // Step 3: Split the linked list
        ListNode[] result = new ListNode[k];
        current = head;
        for (int i = 0; i < k; i++) {
            result[i] = current;
            int partSize = size + (i < remainder ? 1 : 0);
            for (int j = 0; j < partSize - 1 && current != null; j++) {
                current = current.next;
            }
            if (current != null) {
                ListNode nextPart = current.next;
                current.next = null;
                current = nextPart;
            }
        }
        
        return result;
    }
}
