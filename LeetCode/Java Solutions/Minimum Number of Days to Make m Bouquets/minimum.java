import java.util.*;

class Solution {
    public int minDays(int[] bloomDay, int m, int k) {
        if (m * k > bloomDay.length) {
            return -1;
        }

        int low = Integer.MAX_VALUE;
        int high = Integer.MIN_VALUE;

        for (int day : bloomDay) {
            low = Math.min(low, day);
            high = Math.max(high, day);
        }

        while (low < high) {
            int mid = (low + high) / 2;
            if (canMakeBouquets(bloomDay, m, k, mid)) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        return low;
    }

    private boolean canMakeBouquets(int[] bloomDay, int m, int k, int days) {
        int bouquets = 0;
        int flowers = 0;

        for (int bloom : bloomDay) {
            if (bloom <= days) {
                flowers++;
                if (flowers == k) {
                    bouquets++;
                    flowers = 0;
                }
            } else {
                flowers = 0;
            }
        }
        return bouquets >= m;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.minDays(new int[]{1,10,3,10,2}, 3, 1));  // Output: 3
        System.out.println(sol.minDays(new int[]{1,10,3,10,2}, 3, 2));  // Output: -1
        System.out.println(sol.minDays(new int[]{7,7,7,7,12,7,7}, 2, 3));  // Output: 12
        System.out.println(sol.minDays(new int[]{70545,40667,26392,42712,39599,8012,27194,71384,58079,2123,66655,48459,92802,16345,43374,15924,5480,48766,38512,44416,50530,14405,42803,4953,44480,31455,12440,72556,3593,74130,59278,72043,9508,66855,74237,46991,53829,61978,8137,47408,18152,3439,20331,28085,43180,36650,6053,62782,91043,32640,62145,79424,32256,89353,96289,85104,91235,80088,96025,59996,99511,24387,36850,21709,21253,45745,46148,80258,9365,27085,11183,38053,44747,24038,91223,32454,58318,77940,20208,98572,842,31307,90663,46331,8786,32234,24599,30552,78551,67424,19443,45458,49450,37665,79859,70847,30777,96178,96183,3153,98172,11893,35919,10268,21934,2335,50721,26460,73480,27509,19905,83061,64141,28707,73406,30908,80395,26159,41057,91277,5606,5661,88593,16020,69632,8323,15448,15620,70886,54549,73260,7253,60911,91137,20479,12094,8855,1836,28300,41499,91819,73008,74394,5665,52219,15620,54739,52384,58029,92968,17981,62083,91981,96508,19249,60972,39521,13830,15488,6608,13736,51362,27864,52448,51494,79885,95293,3884,70578,22710,744}, 89945, 32127));  // Output: -1
    }
}
