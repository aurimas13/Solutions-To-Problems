The problem description of "Customer Who Visited but Did Not Make Any Transactions" is found [here](https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/description/?envType=study-plan-v2&envId=top-sql-50) while the solution is [here]().

**Explanation**:

1. We're joining the Visits table with the Transactions table using a **LEFT JOIN** on the `visit_id` column.
2. The `WHERE t.transaction_id IS NULL` condition filters the results to only include visits without transactions.
3. We then group the results by `customer_id` using the `GROUP BY` clause.
4. `COUNT(v.visit_id) as count_no_trans` counts the number of visits without transactions for each customer.
5. Finally, we order the results by the count of visits without transactions in descending order, and then by `customer_id` using the **ORDER BY** clause.