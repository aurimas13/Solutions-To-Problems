from typing import List
# Sorting complexity solution: Time & Space - O(n)


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations_length = len(citations)
        papers = [0]*(citations_length+1)

        # Counting papers for each citation number
        for citation in citations:
            # Any citation larger than n can be
            # replaced by citations_length and the h-index will
            # not change after the replacement:
            index = min(citations_length, citation)
            papers[index] += 1

        # Finding the h-index:
        k, s = citations_length, papers[citations_length]
        while k > s:
            k -= 1
            s += papers[k]

        return k


# Running in terminal/console:
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.hIndex(citations=[3, 0, 6, 1, 5])  # citations = [3,0,6,1,5] -> 3 | citations = [1,3,1] -> 1
    print(Solve)
