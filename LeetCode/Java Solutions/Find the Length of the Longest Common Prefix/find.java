class Solution {
    class TrieNode {
        TrieNode[] children = new TrieNode[10];
        int count = 0;
    }
    
    public int longestCommonPrefix(int[] arr1, int[] arr2) {
        TrieNode root = new TrieNode();
        
        // Insert all numbers from arr1 into the Trie
        for (int num : arr1) {
            insert(root, num);
        }
        
        int maxPrefix = 0;
        
        // Check for common prefixes with numbers from arr2
        for (int num : arr2) {
            maxPrefix = Math.max(maxPrefix, findLongestPrefix(root, num));
        }
        
        return maxPrefix;
    }
    
    private void insert(TrieNode node, int num) {
        String s = String.valueOf(num);
        for (char c : s.toCharArray()) {
            int digit = c - '0';
            if (node.children[digit] == null) {
                node.children[digit] = new TrieNode();
            }
            node = node.children[digit];
            node.count++;
        }
    }
    
    private int findLongestPrefix(TrieNode node, int num) {
        String s = String.valueOf(num);
        int length = 0;
        for (char c : s.toCharArray()) {
            int digit = c - '0';
            if (node.children[digit] == null || node.children[digit].count == 0) {
                break;
            }
            node = node.children[digit];
            length++;
        }
        return length;
    }
}