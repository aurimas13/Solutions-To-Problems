from typing import List

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        # Total time spent collecting garbage
        total_time = sum(len(g) for g in garbage)
        
        # Last occurrence of each type of garbage
        last_m, last_p, last_g = -1, -1, -1
        for i, g in enumerate(garbage):
            if 'M' in g:
                last_m = i
            if 'P' in g:
                last_p = i
            if 'G' in g:
                last_g = i
        
        # Add the travel time for each truck
        for i in range(1, len(travel)):
            travel[i] += travel[i-1]
        if last_m != -1:
            total_time += travel[last_m-1] if last_m > 0 else 0
        if last_p != -1:
            total_time += travel[last_p-1] if last_p > 0 else 0
        if last_g != -1:
            total_time += travel[last_g-1] if last_g > 0 else 0

        return total_time
