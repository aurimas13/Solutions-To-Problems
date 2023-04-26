from typing import List
from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # Initialize the email graph and email-to-name mapping
        email_graph = defaultdict(set)
        email_to_name = {}

        # Build the email graph and email-to-name mapping
        for account in accounts:
            name, *emails = account
            for i in range(len(emails)):
                email_graph[emails[0]].add(emails[i])
                email_graph[emails[i]].add(emails[0])
                email_to_name[emails[i]] = name

        # Initialize the visited set and the result list
        visited = set()
        result = []

        # Perform DFS traversal to merge accounts
        def dfs(email, path):
            if email not in visited:
                visited.add(email)
                path.append(email)
                for neighbor in email_graph[email]:
                    dfs(neighbor, path)

        for email in email_graph:
            if email not in visited:
                path = []
                dfs(email, path)
                result.append([email_to_name[email]] + sorted(path))

        return result

# Test cases
if __name__ == '__main__':
    solution = Solution()

    # Test case 1
    accounts1 = [["John", "johnsmith@mail.com", "john00@mail.com"], 
                 ["John", "johnnybravo@mail.com"], 
                 ["John", "johnsmith@mail.com", "john_newyork@mail.com"], 
                 ["Mary", "mary@mail.com"]]
    assert sorted(solution.accountsMerge(accounts1)) == sorted([["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'], 
                                                                 ["John", "johnnybravo@mail.com"], 
                                                                 ["Mary", "mary@mail.com"]])

    print("All test cases passed!")
