import java.util.*;

class Solution {
    public List<Integer> survivedRobotsHealths(int[] positions, int[] healths, String directions) {
        int n = positions.length;
        int[][] robots = new int[n][4];  // {position, health, direction, index}
        for (int i = 0; i < n; i++) {
            robots[i][0] = positions[i];
            robots[i][1] = healths[i];
            robots[i][2] = directions.charAt(i) == 'R' ? 1 : -1;
            robots[i][3] = i;
        }
        Arrays.sort(robots, Comparator.comparingInt(a -> a[0]));
        
        Stack<int[]> stack = new Stack<>();
        for (int[] robot : robots) {
            if (robot[2] == 1) {  // Moving right
                stack.push(robot);
            } else {  // Moving left
                while (!stack.isEmpty() && stack.peek()[2] == 1) {
                    int[] prev = stack.pop();
                    if (prev[1] > robot[1]) {
                        prev[1]--;
                        stack.push(prev);
                        robot[1] = 0;
                        break;
                    } else if (prev[1] < robot[1]) {
                        robot[1]--;
                    } else {  // prev[1] == robot[1]
                        robot[1] = 0;
                        break;
                    }
                }
                if (robot[1] > 0) {
                    stack.push(robot);
                }
            }
        }
        
        List<int[]> result = new ArrayList<>(stack);
        result.sort(Comparator.comparingInt(a -> a[3]));
        
        List<Integer> finalHealths = new ArrayList<>();
        for (int[] robot : result) {
            finalHealths.add(robot[1]);
        }
        return finalHealths;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.survivedRobotsHealths(new int[]{5, 4, 3, 2, 1}, new int[]{2, 17, 9, 15, 10}, "RRRRR"));
        System.out.println(sol.survivedRobotsHealths(new int[]{3, 5, 2, 6}, new int[]{10, 10, 15, 12}, "RLRL"));
        System.out.println(sol.survivedRobotsHealths(new int[]{1, 2, 5, 6}, new int[]{10, 10, 11, 11}, "RLRL"));
    }
}
