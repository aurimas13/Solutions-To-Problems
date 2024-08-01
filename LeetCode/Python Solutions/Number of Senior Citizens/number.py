class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for detail in details:
            age = int(detail[11:13])
            if age > 60:
                count += 1
        return count

# Example usage:
sol = Solution()
details1 = ["7868190130M7522", "5303914400F9211", "9273338290F4010"]
details2 = ["1313579440F2036", "2921522980M5644"]
print(sol.countSeniors(details1))  # Output: 2
print(sol.countSeniors(details2))  # Output: 0
