The problem description of "Confirmation Rate" is found [here](https://leetcode.com/problems/confirmation-rate/description/?envType=study-plan-v2&envId=top-sql-50) while the solution is found [here](https://github.com/aurimas13/Solutions-To-Problems/blob/main/LeetCode/SQL%20Solutions/Confirmation%20Rate/confirmation.sql).

**Explanation**:

1. **Signups Table**: Represents each user's intention to join the newsletter. Every time a user shows interest (maybe by filling out a form on the website), a new entry is made in this table.

2. **Confirmations Table**: Every user in the Signups table will, ideally, have a corresponding entry here. An entry is made every time a user gets a confirmation email, and it records whether they confirmed or if it timed out.

3. **LEFT JOIN**: Since not all users might confirm or even get a confirmation email (maybe due to technical issues), we want to ensure we account for all users from the Signups table, even if they don't have a corresponding entry in the Confirmations table. This is why a LEFT JOIN is used.

4. **Calculating Rates**: For each user, we need to calculate:

- The number of times they confirmed (action = 'confirmed').
- The total number of confirmation emails they received.
The confirmation rate is the ratio of the above two numbers.

5. **Practical Utility**: By getting a report on these confirmation rates:

- The company can understand user engagement.
- Determine if the confirmation process is clear and effective.
- Implement strategies to improve confirmation rates, such as more engaging emails, clearer call-to-action buttons, or improving email delivery rates.

**Practical Implementation**:

Imagine a digital marketing company that sends out monthly newsletters. Before they do, they want to ensure that users genuinely want to receive the emails. So, after a user signs up for the newsletter on the website, an email confirmation request is sent. This is the "double opt-in" method commonly used to ensure user engagement and comply with anti-spam laws. The user can either confirm the subscription (by clicking a link, for example) or ignore it. If they don't confirm within a certain timeframe, the confirmation is marked as "timeout".

The company wants to know the effectiveness of their confirmation process. Are users confirming their subscriptions, or are the requests timing out?

This is essentially our SQL problem:

- `The Signups` table contains information on users who have signed up for the newsletter.
- `The Confirmations` table tracks if the user confirmed their subscription or if it timed out.

The digital marketing company wants to see a rate of confirmation for each user (and in an extended scenario, perhaps even an average for all users or specific user segments).