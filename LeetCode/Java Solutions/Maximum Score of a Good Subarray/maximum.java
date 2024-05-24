import java.util.*;

class Solution {
    public int maxScoreWords(String[] words, char[] letters, int[] score) {
        Map<Character, Integer> letterCount = new HashMap<>();
        for (char letter : letters) {
            letterCount.put(letter, letterCount.getOrDefault(letter, 0) + 1);
        }
        
        return backtrack(words, score, letterCount, 0, 0);
    }
    
    private int backtrack(String[] words, int[] score, Map<Character, Integer> letterCount, int index, int currentScore) {
        if (index == words.length) {
            return currentScore;
        }
        
        int maxScore = backtrack(words, score, letterCount, index + 1, currentScore);
        
        String word = words[index];
        if (canFormWord(word, letterCount)) {
            int wordScore = getWordScore(word, score);
            for (char ch : word.toCharArray()) {
                letterCount.put(ch, letterCount.get(ch) - 1);
            }
            maxScore = Math.max(maxScore, backtrack(words, score, letterCount, index + 1, currentScore + wordScore));
            for (char ch : word.toCharArray()) {
                letterCount.put(ch, letterCount.get(ch) + 1);
            }
        }
        
        return maxScore;
    }
    
    private boolean canFormWord(String word, Map<Character, Integer> letterCount) {
        Map<Character, Integer> wordCount = new HashMap<>();
        for (char ch : word.toCharArray()) {
            wordCount.put(ch, wordCount.getOrDefault(ch, 0) + 1);
        }
        for (Map.Entry<Character, Integer> entry : wordCount.entrySet()) {
            if (letterCount.getOrDefault(entry.getKey(), 0) < entry.getValue()) {
                return false;
            }
        }
        return true;
    }
    
    private int getWordScore(String word, int[] score) {
        int totalScore = 0;
        for (char ch : word.toCharArray()) {
            totalScore += score[ch - 'a'];
        }
        return totalScore;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.maxScoreWords(new String[]{"dog","cat","dad","good"}, new char[]{'a','a','c','d','d','d','g','o','o'}, new int[]{1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0}));  // Output: 23
        System.out.println(sol.maxScoreWords(new String[]{"xxxz","ax","bx","cx"}, new char[]{'z','a','b','c','x','x','x'}, new int[]{4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10}));  // Output: 27
        System.out.println(sol.maxScoreWords(new String[]{"leetcode"}, new char[]{'l','e','t','c','o','d'}, new int[]{0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0}));  // Output: 0
    }
}
