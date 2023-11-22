class Solution {
    public int peakIndexInMountainArray(int[] arr) {
        // Initialize left and right pointers to the start and end of the array.
        int left = 0, right = arr.length - 1;
        
        // Loop until left < right
        while (left < right) {
            // Calculate mid index
            int mid = (left + right) / 2;
            
            // If the value at mid index is smaller than the value at mid+1 index,
            // set left to mid+1, otherwise set right to mid.
            if (arr[mid] < arr[mid+1]) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        
        // The left index, which is also the right index at this point, 
        // is the peak index in the mountain array.
        return left;
    }
}
