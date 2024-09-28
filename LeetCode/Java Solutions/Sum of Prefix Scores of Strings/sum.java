class Solution {
    class TrieNode {
        TrieNode[] children = new TrieNode[26];
        int count = 0;
    }
    
    public int[] sumPrefixScores(String[] words) {
        TrieNode root = new TrieNode();
        
        // Build the Trie
        for (String word : words) {
            insert(root, word);
        }
        
        int[] result = new int[words.length];
        
        // Calculate prefix scores
        for (int i = 0; i < words.length; i++) {
            result[i] = calculateScore(root, words[i]);
        }
        
        return result;
    }
    
    private void insert(TrieNode node, String word) {
        for (char c : word.toCharArray()) {
            int index = c - 'a';
            if (node.children[index] == null) {
                node.children[index] = new TrieNode();
            }
            node = node.children[index];
            node.count++;
        }
    }
    
    private int calculateScore(TrieNode node, String word) {
        int score = 0;
        for (char c : word.toCharArray()) {
            int index = c - 'a';
            if (node.children[index] == null) {
                break;
            }
            node = node.children[index];
            score += node.count;
        }
        return score;
    }
}