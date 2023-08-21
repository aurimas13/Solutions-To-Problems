The problem description of "Queries Quality and Percentage" is found [here](https://leetcode.com/problems/queries-quality-and-percentage/description) and the solution is found [here]().

**Explanation**:

1. **QualityCTE** Common Table Expression:
    - For each `query_name`, we calculate the average of the ratio between rating and `position` to get the query quality. This gives the correct average value for the quality.
    - We use the **CASE** statement to sum the number of queries with a rating less than 3 to get the count of poor queries.
    - We also get the total count of queries for each `query_name` for percentage calculation.

2. In the main query:
    - We round the `quality` value to 2 decimal places as required.
    - We calculate the poor query percentage by taking the ratio of `poor_count` to `total_count` and multiplying by 100. Then, we round the result to 2 decimal places.

**Practical Implementation**:

**Scenario**: **Search Engine Optimization (SEO) Analysis Tool***

Let's say you are developing an SEO analysis tool for content writers and website administrators. This tool allows users to input a series of search queries they want to rank for and then scrapes search engine results for the first 500 positions to see where their webpage ranks and how users rate it (maybe through a plugin you have or some third-party data).

- `query_name`: Represents the keyword or phrase the user wants to rank for.

- `result`: Represents the title of the search result, such as a webpage title.

- `position`: Represents the rank of the result in the search engine.

- `rating`: Could represent the average user click-through rate or satisfaction score for users who visited the page from the search result.

With such data, website administrators can:

- Determine which keywords or queries their content is performing well for.
- Identify queries where their content is appearing in the search results but has a poor click-through rate or user satisfaction score, indicating potential improvements in the content or metadata.

**Implementation**:

1. Data Collection:
    - Web Scraping: Use web scraping tools or APIs (like BeautifulSoup in Python) to gather search results for the inputted queries.
    - Feedback Collection: Integrate with tools like Google Analytics or any other plugin to gather user feedback and calculate the 'rating' for your content.

2. Database Storage:
    - Store this data in a database like MySQL, PostgreSQL, or MongoDB. As your data grows, ensure the database is indexed properly (especially on columns like query_name) to maintain fast query speeds.

3. User Interface:
    - Create a dashboard where users can input queries they want to track, view their content's ranking, quality score, and poor query percentage.
    - Provide actionable insights or suggestions when the poor query percentage is high.

4. Running the Analysis:
    - When a user inputs a new query or requests an analysis, run the SQL query we discussed to provide them with the quality and poor query percentage metrics.
    - Display this data visually, maybe using charts or graphs, for easier user interpretation.

5. Continuous Monitoring:
    - Offer a feature to track these metrics over time. This can show users if changes they've made to their content are positively or negatively affecting their SEO.

6. Integration with other Tools:
    - Allow integration with content management systems (e.g., WordPress, Joomla) so that users can directly modify content based on feedback from the SEO tool.
    - Perhaps provide API access for power users to fetch and analyze this data in their own systems or tools.