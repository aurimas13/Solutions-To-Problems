The problem of "Average Selling Price" descripttion is [here](https://leetcode.com/problems/average-selling-price/description/) while the solution is [here]().

**Explanation**:

- We're joining **UnitsSold** (aliased as `us`) with **Prices** (aliased as `p`) on `product_id` and also making sure the `purchase_date` lies between `start_date` and `end_date` of the **Prices** table. This ensures that for each purchase, we're using the correct price based on the date of purchase.

- In the **SELECT** clause, for each product, we're calculating the total sales as `us.units * p.price` (number of units sold multiplied by the price of each unit) and then summing these up using **SUM(us.units * p.price)** for each product.

- We also calculate the total number of units sold for each product as **SUM(us.units)**.

- To find the average price for each product, we divide the total sales for a product by the total number of units sold for that product. We multiply with 1.0 to ensure that division result is a floating point value.

The **ROUND(..., 2)** function is used to round off the resulting average price to 2 decimal places.


