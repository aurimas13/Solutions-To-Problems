from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        def find_all_concatenated_words(s, words):
            if not s or not words:
                return []

            word_length = len(words[0])
            word_count = len(words)
            total_length = word_length * word_count

            if len(s) < total_length:
                return []

            word_frequency = {}

            for word in words:
                if word not in word_frequency:
                    word_frequency[word] = 0
                word_frequency[word] += 1

            result_indices = []
            for i in range(len(s) - total_length + 1):
                words_seen = {}
                for j in range(0, total_length, word_length):
                    next_word_index = i + j
                    word = s[next_word_index:next_word_index + word_length]

                    if word not in word_frequency:
                        break

                    if word not in words_seen:
                        words_seen[word] = 0
                    words_seen[word] += 1

                    if words_seen[word] > word_frequency.get(word, 0):
                        break

                    if j + word_length == total_length:
                        result_indices.append(i)

            return result_indices

        return find_all_concatenated_words(s, words)


# Write some test cases for your solution 
if __name__ == "__main__":
    def test_solution(s, words, expected):
        s = Solution()
        result = s.findSubstring(s, words)
        assert result == expected, f"Test case failed: expected {expected}, got {result}"
        print("Test case succeeded")

    s = "barfoothefoobarman"
    words = ["foo", "bar"]
    expected = [0, 9]
    test_solution(s, words, expected)
    test_solution("wordgoodgoodgoodbestword", ["word", "good", "best", "word"], [])
    test_solution("barfoofoobarthefoobarman", ["bar", "foo", "the"], [6, 9, 12])