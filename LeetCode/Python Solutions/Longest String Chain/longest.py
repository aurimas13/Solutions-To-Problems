from collections import defaultdict

class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        lentoword = defaultdict(list)
        word2chain = defaultdict(int)
        for word in words:
            lentoword[len(word)].append(word)
        i, stack = len(words[0]), []
        lens = [l for l in lentoword]
        lens.sort()
        self.maxlen = 1
        for item in words:
            word2chain[item] = 1
        for l in lens[1:]:
            if l - 1 in lens:
                for lo in lentoword[l]:
                    self.comparestring(lo, word2chain)
        # print(word2chain)
        return self.maxlen

    def comparestring(self, lo, word2chain):
        for i in range(len(lo)):
            if lo[:i] + lo[i + 1:] in word2chain:
                word2chain[lo] = max(word2chain[lo], word2chain[lo[:i] + lo[i + 1:]] + 1)
                self.maxlen = max(self.maxlen, word2chain[lo])
        return


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.longestStrChain(["a","b","ba","bca","bda","bdca"])  # ["a","b","ba","bca","bda","bdca"] -> 4 | ["xbc","pcxbcf","xb","cxbc","pcxbc"] -> 5
    print(Solve)
