import java.util.ArrayList;
import java.util.List;

public class Solution {
    public List<String> letterCombinations(String digits) {
        // Return an empty list if there are no digits
        if (digits == null || digits.length() == 0) {
            return new ArrayList<>();
        }

        // Define the mapping of digits to letters
        String[] letters = {
            null,
            null,
            "abc",
            "def",
            "ghi",
            "jkl",
            "mno",
            "pqrs",
            "tuv",
            "wxyz"
        };

        // Initialize a list to store the iterables (strings) corresponding to the digits
        List<String> iterables = new ArrayList<>();
        for (char n : digits.toCharArray()) {
            iterables.add(letters[Character.getNumericValue(n)]);
        }

        // Initialize the result list
        List<String> result = new ArrayList<>();
        // Call the recursive function to generate the combinations
        backtrack("", iterables, 0, result);

        return result;
    }

    // Recursive function to generate combinations
    private void backtrack(String currentCombination, List<String> iterables, int index, List<String> result) {
        // If the current combination is of the required length, add it to the result
        if (index == iterables.size()) {
            result.add(currentCombination);
            return;
        }

        // Iterate through the letters at the current index and generate combinations
        String currentLetters = iterables.get(index);
        for (char c : currentLetters.toCharArray()) {
            // Append the current letter and recurse
            backtrack(currentCombination + c, iterables, index + 1, result);
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.letterCombinations("23")); // Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    }
}


