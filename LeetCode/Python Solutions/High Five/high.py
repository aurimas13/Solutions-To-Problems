from typing import List
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        d = defaultdict(list)
        for i in items:
            d[i[0]].append(i[1])
        return ([[key, int(sum(sorted(d[key], reverse=True)[:5]) / 5)] for key in sorted(d.keys())])


# Running in terminal/console:
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.highFive(items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]  #items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]] -> [[1,87],[2,88]]
    print(Solve)

