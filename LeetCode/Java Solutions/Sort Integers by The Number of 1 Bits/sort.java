import java.util.Arrays;

class Solution {
    public int[] sortByBits(int[] arr) {
        // Sorting using custom comparator
        Integer[] boxedArr = Arrays.stream(arr).boxed().toArray(Integer[]::new);
        Arrays.sort(boxedArr, (a, b) -> {
            int countA = Integer.bitCount(a);
            int countB = Integer.bitCount(b);
            if (countA == countB) return a - b;
            return countA - countB;
        });
        return Arrays.stream(boxedArr).mapToInt(Integer::intValue).toArray();
    }
}


