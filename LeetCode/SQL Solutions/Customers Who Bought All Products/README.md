The problem description of "Customers Who Bought All Products" is found [here](https://leetcode.com/problems/customers-who-bought-all-products/description/) while the solution is found [here]().

**Explanation**:

1. GROUP BY customer_id: This groups the records in the Customer table by customer_id, so we can count the number of distinct products each customer bought.

2. HAVING COUNT(DISTINCT product_key): This counts the number of distinct products for each customer.
(SELECT COUNT(*) FROM Product): This subquery counts the total number of products available.

3. The main query then compares the count from each customer with the total number of products. If they match, the customer ID is selected.

**Implementation**:

Let's say we have a small online store that sells two products: Product 5 and Product 6.

Customer 1 bought both Product 5 and Product 6.
Customer 2 only bought Product 6.
Customer 3 bought both Product 5 and Product 6.
When we run the above SQL query on this data, it will return:

```sql 
customer_id
-----------
1
3
```

This result indicates that only Customer 1 and Customer 3 bought all the products available in the store.