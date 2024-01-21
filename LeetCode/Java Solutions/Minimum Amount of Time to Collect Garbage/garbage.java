class Solution {
    public int garbageCollection(String[] garbage, int[] travel) {
        int total_time = 0;

        // Calculate total time spent collecting garbage
        for (String g : garbage) {
            total_time += g.length();
        }

        // Last occurrence of each type of garbage
        int last_m = -1, last_p = -1, last_g = -1;
        for (int i = 0; i < garbage.length; i++) {
            String g = garbage[i];
            if (g.contains("M")) {
                last_m = i;
            }
            if (g.contains("P")) {
                last_p = i;
            }
            if (g.contains("G")) {
                last_g = i;
            }
        }

        // Add the travel time for each truck
        total_time += calculateTravelTime(travel, last_m);
        total_time += calculateTravelTime(travel, last_p);
        total_time += calculateTravelTime(travel, last_g);

        return total_time;
    }

    private int calculateTravelTime(int[] travel, int lastIndex) {
        int time = 0;
        for (int i = 0; i < lastIndex; i++) {
            time += travel[i];
        }
        return time;
    }
}
