The problem description of "Customer Who Visited but Did Not Make Any Transactions" is found [here](https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/description/?envType=study-plan-v2&envId=top-sql-50) while the solution is [here]().

**Explanation**:

1. We're joining the Visits table with the Transactions table using a **LEFT JOIN** on the `visit_id` column.
2. The `WHERE t.transaction_id IS NULL` condition filters the results to only include visits without transactions.
3. We then group the results by `customer_id` using the `GROUP BY` clause.
4. `COUNT(v.visit_id) as count_no_trans` counts the number of visits without transactions for each customer.
5. Finally, we order the results by the count of visits without transactions in descending order, and then by `customer_id` using the **ORDER BY** clause.

**Practical Implementation**:

*Scenartio:* A bookstore offers a loyalty program where registered customers get points for each visit, even if they don't make a purchase. However, customers earn extra points when they do make a purchase. The bookstore wants to identify and possibly engage those customers who visit frequently without making a purchase, as these customers demonstrate interest but might have barriers to buying. The management decides to send them special offers, hoping to convert their visits into sales.

*Solution:* Using this query - the bookstore can identify registered customers who have visited multiple times without making any purchase. For example, if customer 103 has visited 5 times without buying anything, they might be sent a special discount code or a personalized recommendation to entice them to buy on their next visit.

This strategy helps the bookstore understand customer behavior better and tailor its marketing initiatives accordingly.
