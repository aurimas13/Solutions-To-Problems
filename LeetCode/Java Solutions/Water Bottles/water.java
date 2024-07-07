class Solution {
    public int numWaterBottles(int numBottles, int numExchange) {
        int totalDrunk = numBottles;
        int emptyBottles = numBottles;
        
        while (emptyBottles >= numExchange) {
            int newFullBottles = emptyBottles / numExchange;
            totalDrunk += newFullBottles;
            emptyBottles = emptyBottles % numExchange + newFullBottles;
        }
        
        return totalDrunk;
    }
}
