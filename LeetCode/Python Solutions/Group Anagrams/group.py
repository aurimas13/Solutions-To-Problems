from typing import List
class Solution:
    def sort_word(self, word):
        return ''.join(sorted(word))

    def update_anagrams_dict(self, anagrams_dict, sorted_word, word):
        if sorted_word in anagrams_dict:
            value_arr = anagrams_dict[sorted_word]
            value_arr.append(word)
            anagrams_dict[sorted_word] = value_arr
        else:
            anagrams_dict[sorted_word] = [word]

        return anagrams_dict

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = {}
        for word in strs:
            sorted_word = self.sort_word(word)
            anagrams_dict = self.update_anagrams_dict(anagrams_dict,
                                                      sorted_word,
                                                      word)

        result = []
        for key in anagrams_dict:
            result.append(anagrams_dict[key])

        return result\


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"])  # strs = ["eat","tea","tan","ate","nat","bat"] -> [["bat"],["nat","tan"],["ate","eat","tea"]] | ["a"] -> [["a"]]
    print(Solve)
