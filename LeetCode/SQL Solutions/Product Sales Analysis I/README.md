The problem description of "Product Sales Analysis I" is [here](https://leetcode.com/problems/product-sales-analysis-i/?envType=study-plan-v2&envId=top-sql-50) while the solution is [here](https://github.com/aurimas13/Solutions-To-Problems/blob/main/LeetCode/SQL%20Solutions/Product%20Sales%20Analysis%20I/product.sql).


**Explanation:**
1. `SELECT` Clause:
This clause defines the columns we wish to appear in the result set.

`p.product_name`: Retrieves the names of the products.
`s.year`: Retrieves the year when the sale was made.
`s.price`: Retrieves the price at which the product was sold.

Here, we've prefixed each column with an alias (p or s) to specify which table the column is coming from.

2. `FROM` Clause:
This clause identifies the tables from which the data will be fetched.

`Product p`: This indicates that we're pulling data from the Product table and we're giving this table an alias, p.
Aliases are convenient for a couple of reasons:

They can make the query shorter and more readable, especially if table names are long or if you are working with multiple tables.
They prevent ambiguity when two tables have columns with the same name.

3. `JOIN` Clause:
Joins allow you to combine rows from two or more tables based on related columns between them. This query uses an `INNER JOIN` which means it will only return rows where there is a match in both tables.

`JOIN Sales s`: This tells SQL that we want to join with the Sales table. We're giving the Sales table an alias, s.
ON p.product_id = s.product_id: This is the condition for the join. We're joining the two tables based on the product_id column. In simple terms, it matches every sale with its corresponding product using the product_id.

4. `ORDER BY` Clause:
This clause specifies how the result set should be sorted.

`p.product_name`: This means that the results will first be ordered by the product name in ascending order (alphabetically).
`s.year`: If two rows have the same product name, they'll then be sorted by year in ascending order.

**Practical Interpretation**:

Imagine you're in a bookstore with a sales register. Each sale is logged with information about which book was sold, when, and at what price. Each book has an ID, a unique identifier. In another record, you have details about each book, including its ID and its name.

Now, if someone asks, "Can you show me the names of the books that were sold, the year they were sold, and at what price, sorted by the name of the book and then the year?", this SQL query does precisely that.

It starts with the book details, matches them with the sales register using the book ID, fetches the name of the book, the year of the sale, and the price, and then presents this information sorted by the book name and year.