from typing import List


class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:

        event1Start = event1[0].split(':')
        event1End = event1[1].split(':')

        event2Start = event2[0].split(':')
        event2End = event2[1].split(':')

        return False if event2Start > event1End or event1Start > event2End else True


# Tests:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.haveConflict(event1 = ["01:15","02:00"], event2 = ["02:00","03:00"])
    # event1 = ["01:15","02:00"], event2 = ["02:00","03:00"] -> true
    # event1 = ["10:00","11:00"], event2 = ["14:00","15:00"] -> false
    print(Solve)