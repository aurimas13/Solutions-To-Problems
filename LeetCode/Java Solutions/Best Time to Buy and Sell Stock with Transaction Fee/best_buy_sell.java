public class Solution {
    public int maxProfit(int[] prices, int fee) {
        // We initialize cash and hold, cash represents the maximum profit we could have if we did not have a share of stock,
        // hold represents the maximum profit we could have if we owned a share of stock.
        int cash = 0, hold = -prices[0];
        
        for(int i = 1; i < prices.length; i++) {
            // For each day, we may not do anything, or sell our stock and buy it again.
            // If we sell our stock, we have price[i] extra cash, but we have to pay the fee. 
            // The new value of cash is either its old value, or this new possible value. 
            // At the end of the loop, cash is the answer to our problem.
            cash = Math.max(cash, hold + prices[i] - fee);
            
            // If we buy a stock, we have to pay price[i] units of cash. 
            // So the new value of hold is either its old value, or this new possible value. 
            hold = Math.max(hold, cash - prices[i]);
        }
        
        // return the maximum profit if we did not have a share of stock.
        return cash;
    }
}
