# Solution
import collections
from typing import List


class Solution:
    @staticmethod
    def accountsMerge(accounts: List[List[str]]) -> List[List[str]]:
        n2a = collections.defaultdict(list)
        for account in accounts:
            eset = set(account[1:])

            if account[0] in n2a:
                accset = n2a[account[0]]
                removelist = [emails for emails in accset if eset.intersection(emails)]

                for emails in removelist:
                    eset |= emails
                    accset.remove(emails)
            n2a[account[0]] += [eset]
        return [[name] + sorted(emails) for name in n2a for emails in n2a[name]]


# Checking in Console
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.accountsMerge(accounts = [
        ["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"],
        ["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],
        ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"],
        ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"],
        ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"]])
    # Output: [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],
    # ["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],
    # ["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],
    # ["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],
    # ["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]
    print(Solve)
