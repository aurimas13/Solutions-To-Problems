import java.util.ArrayList;
import java.util.List;

class Solution {
    public static List<String> wordBreak(String s, List<String> wordDict) {
        List<List<String>> dp = new ArrayList<>();
        for (int i = 0; i <= s.length(); i++) {
            dp.add(new ArrayList<>());
        }
        dp.get(0).add("");

        for (int i = 0; i < dp.size(); i++) {
            if (!dp.get(i).isEmpty()) {
                for (String word : wordDict) {
                    int offset = word.length();
                    if (i + offset <= s.length() && s.substring(i, i + offset).equals(word)) {
                        for (String sentence : dp.get(i)) {
                            dp.get(i + offset).add(sentence + (sentence.isEmpty() ? "" : " ") + word);
                        }
                    }
                }
            }
        }

        return dp.get(s.length());
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        List<String> wordDict1 = new ArrayList<>();
        wordDict1.add("apple");
        wordDict1.add("pen");
        wordDict1.add("applepen");
        wordDict1.add("pine");
        wordDict1.add("pineapple");
        
        List<String> result1 = sol.wordBreak("pineapplepenapple", wordDict1);
        System.out.println(result1);

        List<String> wordDict2 = new ArrayList<>();
        wordDict2.add("cats");
        wordDict2.add("dog");
        wordDict2.add("sand");
        wordDict2.add("and");
        wordDict2.add("cat");
        
        List<String> result2 = sol.wordBreak("catsandog", wordDict2);
        System.out.println(result2);
    }
}
