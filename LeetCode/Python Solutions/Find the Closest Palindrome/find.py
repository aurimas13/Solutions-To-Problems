class Solution:
    def nearestPalindromic(self, n: str) -> str:
        if len(n) == 1:
            return str(int(n) - 1)
        
        l = len(n)
        candidates = [10**(l-1) - 1, 10**l + 1]  # Edge cases
        
        prefix = int(n[:(l+1)//2])
        for i in range(prefix-1, prefix+2):
            if l % 2 == 0:
                candidate = int(str(i) + str(i)[::-1])
            else:
                candidate = int(str(i) + str(i)[-2::-1])
            candidates.append(candidate)
        
        num = int(n)
        return str(min((c for c in candidates if c != num), key=lambda x: (abs(x-num), x)))