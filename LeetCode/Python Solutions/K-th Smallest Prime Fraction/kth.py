class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # Base case: the first symbol is always 0.
        if n == 1:
            return 0
        
        # Calculate the parent's position and what the parent is
        parent = self.kthGrammar(n - 1, (k + 1) // 2)
        
        # If the parent is 0, the sequence is 01. If it's 1, the sequence is 10.
        # The kth symbol is checking if k is odd or even to determine its position in the sequence.
        if parent == 0:
            return 0 if k % 2 == 1 else 1
        else:
            return 1 if k % 2 == 1 else 0
        

        