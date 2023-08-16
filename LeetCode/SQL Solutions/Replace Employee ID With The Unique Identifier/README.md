The problem description of "Replace Employee ID With The Unique Identifier" is [here](https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/?envType=study-plan-v2&envId=top-sql-50) while the solution is [here](https://github.com/aurimas13/Solutions-To-Problems/blob/main/LeetCode/SQL%20Solutions/Replace%20Employee%20ID%20With%20The%20Unique%20Identifier/replace.sql).

**Explanation:**

- `FROM Employees e`: This means we're selecting from the *Employees* table and we're giving it an alias e for convenience.

- `LEFT JOIN EmployeeUNI eu ON e.id = eu.id`: Here, we're performing a **LEFT JOIN** with the *EmployeeUNI* table (with alias eu). This join is based on matching ids between both tables. A **LEFT JOIN** ensures that even if an employee in the Employees table doesn't have a corresponding entry in the *EmployeeUNI* table, they will still appear in the results (with a NULL unique_id).

- `SELECT eu.unique_id AS unique_id, e.name AS name`: This portion specifies which columns we want in the final result. We're selecting the unique_id from *EmployeeUNI* and the name from *Employees*. We're also renaming them in the result set using the **AS** keyword for clarity, though in this case, the names remain the same.

**Practical Implementation**:

A hospital uses an old patient management system that assigns a simple, incremental patient ID (*id*) to every individual admitted. The hospital decides to upgrade its system for improved data privacy and protection, introducing a new system that generates a more secure, non-sequential unique patient identifier (*unique_id*).

However, during the transition period, both the old and new systems are in use. The hospital maintains two tables:

*Patients*: Contains the old patient IDs (id) and patient names (name).
*PatientUNI*: Contains a mapping between the old patient IDs (id) and the new unique identifiers (unique_id).

For a time, the hospital staff may need to pull up patient details based on both the old ID and the new unique ID, especially if some departments have switched to the new system while others are still using the old one.

By running this query, hospital staff can efficiently handle inquiries, data tracking, and management tasks during the transition phase. For instance, when a patient comes to the hospital and gives their old patient ID, the staff can quickly cross-reference and determine their new unique ID, or verify if it's been generated yet.

This type of merging or cross-referencing based on common identifiers is a recurring theme in many industries, especially during transitions, upgrades, or system integrations.