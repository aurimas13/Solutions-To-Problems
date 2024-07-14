from collections import defaultdict

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def parse():
            N = len(formula)
            i = 0
            stack = [defaultdict(int)]
            
            while i < N:
                if formula[i] == '(':
                    stack.append(defaultdict(int))
                    i += 1
                elif formula[i] == ')':
                    i += 1
                    start = i
                    while i < N and formula[i].isdigit():
                        i += 1
                    multiplicity = int(formula[start:i] or 1)
                    top = stack.pop()
                    for name, v in top.items():
                        stack[-1][name] += v * multiplicity
                else:
                    start = i
                    i += 1
                    while i < N and formula[i].islower():
                        i += 1
                    name = formula[start:i]
                    start = i
                    while i < N and formula[i].isdigit():
                        i += 1
                    multiplicity = int(formula[start:i] or 1)
                    stack[-1][name] += multiplicity
            
            return stack[0]

        counts = parse()
        return ''.join(name + (str(counts[name]) if counts[name] > 1 else '')
                       for name in sorted(counts))

# Example usage:
sol = Solution()
print(sol.countOfAtoms("H2O"))         # Output: "H2O"
print(sol.countOfAtoms("Mg(OH)2"))     # Output: "H2MgO2"
print(sol.countOfAtoms("K4(ON(SO3)2)2")) # Output: "K4N2O14S4"
