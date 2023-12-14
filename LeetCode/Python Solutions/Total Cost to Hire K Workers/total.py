from typing import List
from heapq import heapify, heappop, heappush

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        # If the number of candidates is equal to or greater than half of the total workers,
        # we can hire all the candidates and select the k cheapest workers
        if candidates * 2 >= len(costs):
            costs.sort()
            return sum(costs[:k])
        else:
            pointer1 = candidates - 1
            pointer2 = len(costs) - candidates

            arr1, arr2 = costs[:candidates], costs[-candidates:]

            heapify(arr1)
            heapify(arr2)
            res = 0

            for _ in range(k):
                if arr1 and arr2:
                    if arr1[0] <= arr2[0]:
                        res += heappop(arr1)
                        pointer1 += 1
                        if pointer1 < pointer2:
                            heappush(arr1, costs[pointer1])
                    else:
                        res += heappop(arr2)
                        pointer2 -= 1
                        if pointer1 < pointer2:
                            heappush(arr2, costs[pointer2])
                else:
                    if arr1:
                        res += heappop(arr1)
                    else:
                        res += heappop(arr2)

            return res
