The problem description of "Fix Names in a Table" is found [here](https://leetcode.com/problems/fix-names-in-a-table/description/) while the solution is found [here](https://github.com/aurimas13/Solutions-To-Problems/blob/main/LeetCode/SQL%20Solutions/Fix%20Names%20in%20a%20Table/fix.sql).

**Explanation**:

1. `UPPER(SUBSTRING(name, 1, 1))`: This extracts the first character from the name column and changes it to uppercase using the UPPER() function.

2. `LOWER(SUBSTRING(name, 2))`: This extracts all characters from the name column starting from the second character and changes them to lowercase using the LOWER() function.

3. `CONCAT()`: This function combines the uppercase first letter with the rest of the lowercase letters.

**Implementation**:

Imagine a registration system for a conference. Attendees register online, and they can type in their name in any format. Some may type "JOHN", others "john", and others "JoHN". However, when printing name tags or certificates for the attendees, it's more professional to have a standardized format, such as "John".

By using the above SQL query, the organizer can easily generate a list of names in the desired format without needing to manually adjust each one. This ensures consistency and professionalism across all materials and interactions.