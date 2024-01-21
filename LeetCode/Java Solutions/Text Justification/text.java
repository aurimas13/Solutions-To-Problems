import java.util.*;

class Solution {
    public List<String> fullJustify(String[] words, int maxWidth) {
        List<String> result = new ArrayList<>();
        List<String> currentLine = new ArrayList<>();
        int num_of_letters = 0;

        for (String word : words) {
            // Check if the current word can fit into the current line (including spaces).
            if (num_of_letters + word.length() + currentLine.size() > maxWidth) {
                // Distribute spaces
                for (int i = 0; i < maxWidth - num_of_letters; i++) {
                    // Get the index for space addition
                    int index = i % (currentLine.size() - 1 == 0 ? 1 : currentLine.size() - 1);
                    // Update the word at that index
                    currentLine.set(index, currentLine.get(index) + " ");
                }
                
                StringBuilder sb = new StringBuilder();
                for (String w : currentLine) {
                    sb.append(w);
                }
                result.add(sb.toString());
                currentLine.clear();
                num_of_letters = 0;
            }
            currentLine.add(word);
            num_of_letters += word.length();
        }

        // Left justify the last line
        StringBuilder sb = new StringBuilder(String.join(" ", currentLine));
        while (sb.length() < maxWidth) {
            sb.append(" ");
        }
        result.add(sb.toString());

        return result;
    }
}


