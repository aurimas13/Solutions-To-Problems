from typing import List
from collections import defaultdict

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        prime_to_indices = defaultdict(list)

        # Function to factorize a number and update prime_to_indices mapping
        def factorize(num):
            factors = set()
            d = 2
            while d * d <= num:
                while num % d == 0:
                    factors.add(d)
                    num //= d
                d += 1
            if num > 1:
                factors.add(num)
            return factors
        
        # Populate prime_to_indices with factors of each number
        for i, num in enumerate(nums):
            for factor in factorize(num):
                prime_to_indices[factor].append(i)
        
        # Union-Find data structure
        parent = list(range(n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parent[find(x)] = find(y)
        
        # Union indices with common prime factors
        for indices in prime_to_indices.values():
            for i in range(1, len(indices)):
                union(indices[i], indices[i-1])
        
        # Check if all numbers are connected
        root = find(0)
        for i in range(1, n):
            if find(i) != root:
                return False
        return True
