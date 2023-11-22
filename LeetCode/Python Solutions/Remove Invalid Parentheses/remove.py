from typing import List


class Solution:
    @staticmethod
    def removeInvalidParentheses(s: str) -> List[str]:
        def reverse_par(s):
            def norm(c):
                if c == '(':
                    return ')'
                elif c == ')':
                    return '('
                else:
                    return c

            return ''.join(norm(c) for c in reversed(s))

        def fix_neg(s):
            balance = 0
            fixes = []
            neg_indices = []
            for i, c in enumerate(s):
                if c == '(':
                    balance += 1
                elif c == ')':
                    neg_indices.append(i)
                    balance -= 1
                    if balance < 0:
                        for idx in neg_indices:
                            fixes.extend(fix_neg(s[:idx] + s[idx + 1:]))
                        return fixes
            fixes.append(s)
            return fixes

        perm = set()
        for ss in set(fix_neg(s)):
            perm.update([reverse_par(rev) for rev in set(fix_neg(reverse_par(ss)))])
        return list(perm)


# # Checking in console
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.removeInvalidParentheses(s = "(a)())()")
    # s = "(a)())()" -> ["(a())()","(a)()()"] | s = ")(" -> [""]
    print(Solve)
