class Solution {
    public ListNode removeZeroSumSublists(ListNode head) {
        ListNode dummy = new ListNode(0); // Create a dummy head to simplify edge cases
        dummy.next = head;
        // HashMap to store the last node for each prefix sum
        HashMap<Integer, ListNode> prefixSumMap = new HashMap<>();
        prefixSumMap.put(0, dummy);
        
        int sum = 0;
        // First pass: Build the prefix sum map
        for (ListNode curr = head; curr != null; curr = curr.next) {
            sum += curr.val;
            prefixSumMap.put(sum, curr);
        }
        
        sum = 0;
        // Second pass: Remove zero sum sublists
        for (ListNode curr = dummy; curr != null; curr = curr.next) {
            sum += curr.val;
            curr.next = prefixSumMap.get(sum).next;
        }
        
        return dummy.next;
    }
}