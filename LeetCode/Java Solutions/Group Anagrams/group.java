import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> anagrams = new HashMap<>();

        for (String word : strs) {
            char[] charArray = word.toCharArray();
            Arrays.sort(charArray);  // Sort the characters of the word
            String sortedWord = new String(charArray);
            
            // If the sorted word is not in the map, add it with a new list
            if (!anagrams.containsKey(sortedWord)) {
                anagrams.put(sortedWord, new ArrayList<>());
            }
            // Add the original word to the list associated with the sorted word
            anagrams.get(sortedWord).add(word);
        }

        return new ArrayList<>(anagrams.values());  // Return grouped anagrams
    }
}
