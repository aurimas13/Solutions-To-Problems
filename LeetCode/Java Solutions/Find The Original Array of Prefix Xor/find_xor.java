class Solution {
    public int[] findArray(int[] pref) {
        int n = pref.length;
        int[] arr = new int[n];
        arr[0] = pref[0];  // for i=0, arr[0] is same as pref[0]
        for (int i = 1; i < n; i++) {
            arr[i] = pref[i] ^ pref[i-1];
        }
        return arr;
    }
}
