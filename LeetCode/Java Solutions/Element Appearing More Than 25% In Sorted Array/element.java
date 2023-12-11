class Solution {
    public int findSpecialInteger(int[] arr) {
        int n = arr.length;
        int threshold = n / 4;

        int currentCount = 1;
        for (int i = 1; i < n; i++) {
            if (arr[i] == arr[i - 1]) {
                currentCount++;
                if (currentCount > threshold) {
                    return arr[i];
                }
            } else {
                currentCount = 1;
            }
        }

        return arr[0]; // Handle case for single element array
    }
}

