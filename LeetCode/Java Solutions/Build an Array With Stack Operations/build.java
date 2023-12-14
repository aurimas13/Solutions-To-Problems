import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<String> buildArray(int[] target, int n) {
        List<String> operations = new ArrayList<>();
        int current = 0;  // Pointer for the current element in the target array

        for (int num = 1; num <= n; num++) {
            if (current >= target.length) {
                break;  // Stop if we have reached the end of the target array
            }
            operations.add("Push");
            if (target[current] == num) {
                current++;  // Move to the next target element
            } else {
                operations.add("Pop");  // Pop if the number is not in the target
            }
        }

        return operations;
    }
}