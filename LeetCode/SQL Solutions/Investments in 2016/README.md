The problem description of "Investments in 2016". is found [here](https://leetcode.com/problems/investments-in-2016/description/) while the solution is found [here]().

**Explanation**:

The first subquery (with tiv_2015) fetches the values of tiv_2015 which appear more than once. The second subquery (with (lat, lon)) fetches the unique coordinates.

Then, the main query filters out the records based on the output from the two subqueries and sums up the tiv_2016 values for the selected records.

**Implementation**:

Consider an insurance company that provides property insurance. The value of properties can change over time, and the company keeps a track of these values. The company might want to analyze which policyholders with the same insured values in the year 2015 are located in different cities (hence unique lat-lon pairs) and get the total insured value for the year 2016 for these policyholders. This could be to identify any risk concentration or even analyze how values have shifted over a year for properties with the same insured value in the previous year.