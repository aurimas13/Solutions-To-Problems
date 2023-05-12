class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
         # Generate Fibonacci sequence up to k
        fib = [1, 1]
        while fib[-1] < k:
            fib.append(fib[-1] + fib[-2])
        
        # Use a greedy approach to choose largest Fibonacci numbers that fit into remaining sum
        count = 0
        i = len(fib) - 1
        while k > 0:
            if fib[i] <= k:
                k -= fib[i]
                count += 1
            i -= 1
        
        return count


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.findMinFibonacciNumbers(k = 7) # k = 7 -> 2 
    # k = 10 -> 2 
    print(Solve)
