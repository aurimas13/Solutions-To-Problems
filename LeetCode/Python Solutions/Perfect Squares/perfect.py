from collections import deque


class Solution:
    def numSquares(self, n: int) -> int:
        cands = list([i * i for i in range(1, 101) if i * i <= n])
        lvl = 0
        dq = deque([n])
        seen = set([n])
        while dq:
            sz = len(dq)
            for _ in range(sz):
                elem = dq.popleft()
                if elem == 0:
                    return lvl
                for c in cands:
                    if c > elem:
                        break
                    else:
                        new_elem = elem - c
                        if new_elem not in seen:
                            seen.add(new_elem)
                            dq.append(new_elem)
            lvl += 1

        return lvl


# Checking in console
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.numSquares(n = 13)
    # n = 13 -> 2
    # n = 12 -> 3
    print(Solve)
