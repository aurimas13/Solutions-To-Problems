class Solution:
    @staticmethod
    def numTrees(n: int) -> int:
        numTree=[1]*(n+1)
        for nodes in range(2,n+1):
            total=0
            for root in range(1,nodes+1):
                left=root-1
                right= nodes-root
                total+=numTree[left]*numTree[right]
                numTree[nodes]=total
        return numTree[n]


if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.numTrees(n = 3)
    # n = 3 -> 5
    # n = 1 -> 1
    print(Solve)
