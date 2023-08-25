The problem description of "Game Play Analysis IV" is found [here](https://leetcode.com/problems/game-play-analysis-iv/description/?envType=study-plan-v2&envId=top-sql-50) while the solution is found [here]().

**Explanation**:

1. **FirstLogin CTE**:

- This Common Table Expression (CTE) finds the earliest (i.e., first) login date for each player.
- MIN(event_date) finds the earliest date for each player, and then it groups by player_id.

2. **ConsecutiveLogin CTE**:

- This CTE checks if a player has an entry for the day after their first login day.
- It joins the Activity table with FirstLogin based on player_id.
- The WHERE clause checks if the event_date from the Activity table is exactly one day after the first login day (first_day from the FirstLogin).

3. **Final Query**:

- It joins the two CTEs based on player_id.
- It calculates the required fraction by dividing the number of players who have logged in consecutively by the total number of players. The ROUND(..., 2) function is used to round the fraction to two decimal places.

**Implementation**:

Let's consider a real-world scenario: An online learning platform wants to measure user engagement in the first few days of signing up. They believe that if users engage with the platform on consecutive days immediately after signing up, they are more likely to continue using the platform in the long run. By calculating the fraction of users who log in on consecutive days after their sign-up, they can gauge the initial appeal and effectiveness of their onboarding process. If this fraction is low, they might consider improving their onboarding tutorials or offering incentives to get users back on the platform.