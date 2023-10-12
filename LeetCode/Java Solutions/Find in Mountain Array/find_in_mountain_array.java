/**
 * // This is the MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * interface MountainArray {
 *     public int get(int index);
 *     public int length();
 * }
 */

public class Solution {
    public int findInMountainArray(int target, MountainArray mountainArr) {
        // Binary search to find the peak of the mountain
        int l = 0, r = mountainArr.length() - 1;
        while (l < r) {
            int mid = (l + r) / 2;
            if (mountainArr.get(mid) < mountainArr.get(mid + 1)) {
                l = mid + 1;
            } else {
                r = mid;
            }
        }
        
        int peak = l;

        // Binary search in the ascending part of the mountain
        l = 0;
        r = peak;
        while (l <= r) {
            int mid = (l + r) / 2;
            int currVal = mountainArr.get(mid);
            if (currVal == target) {
                return mid;
            } else if (currVal < target) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }

        // Binary search in the descending part of the mountain
        l = peak;
        r = mountainArr.length() - 1;
        while (l <= r) {
            int mid = (l + r) / 2;
            int currVal = mountainArr.get(mid);
            if (currVal == target) {
                return mid;
            } else if (currVal < target) {
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }

        return -1;
    }
}

