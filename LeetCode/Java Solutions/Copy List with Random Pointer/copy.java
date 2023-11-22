class Solution {
    public Node copyRandomList(Node head) {
        if (head == null) return null;  // if head is null, return null

        // Step 1: Create duplicate nodes next to original nodes
        Node curr = head;
        while (curr != null) {
            Node new_node = new Node(curr.val);
            new_node.next = curr.next;
            curr.next = new_node;
            curr = new_node.next;
        }

        // Step 2: Adjust the random pointers for all duplicate nodes
        curr = head;
        while (curr != null) {
            if (curr.random != null) {
                curr.next.random = curr.random.next;
            }
            curr = curr.next.next;
        }

        // Step 3: Detach duplicate nodes to form the deep copied list
        Node old_list = head;
        Node new_list = head.next;
        Node new_head = head.next;
        while (old_list != null) {
            old_list.next = old_list.next.next;
            if (new_list.next != null) {
                new_list.next = new_list.next.next;
            }
            old_list = old_list.next;
            new_list = new_list.next;
        }

        return new_head;
    }
}
