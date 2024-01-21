class Solution {
    public int sumSubarrayMins(int[] arr) {
        final int MOD = 1000000007;
        int n = arr.length;
        int[] prevSmaller = new int[n];
        int[] nextSmaller = new int[n];
        Deque<Integer> stack = new ArrayDeque<>();

        // Initialize next smaller elements as n, which means no next smaller element
        Arrays.fill(nextSmaller, n);

        // Find previous smaller element for each element
        for (int i = 0; i < n; ++i) {
            while (!stack.isEmpty() && arr[stack.peek()] > arr[i]) {
                stack.pop();
            }
            prevSmaller[i] = stack.isEmpty() ? -1 : stack.peek();
            stack.push(i);
        }

        // Clear the stack for the next pass
        stack.clear();

        // Find next smaller element for each element
        for (int i = 0; i < n; ++i) {
            while (!stack.isEmpty() && arr[stack.peek()] > arr[i]) {
                nextSmaller[stack.pop()] = i;
            }
            stack.push(i);
        }

        // Calculate the sum of minimums of all subarrays
        long ans = 0;
        for (int i = 0; i < n; ++i) {
            long countLeft = i - prevSmaller[i];
            long countRight = nextSmaller[i] - i;
            ans = (ans + countLeft * countRight % MOD * arr[i] % MOD) % MOD;
        }

        return (int) ans;
    }
}
