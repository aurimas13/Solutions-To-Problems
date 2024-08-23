from math import gcd
from fractions import Fraction

class Solution:
    def fractionAddition(self, expression: str) -> str:
        # Add '+' at the beginning if the expression doesn't start with a sign
        if expression[0] not in '+-':
            expression = '+' + expression
        
        # Parse fractions
        fractions = []
        i = 0
        while i < len(expression):
            sign = 1 if expression[i] == '+' else -1
            i += 1
            j = i
            while j < len(expression) and expression[j] != '+' and expression[j] != '-':
                j += 1
            num, den = map(int, expression[i:j].split('/'))
            fractions.append(Fraction(sign * num, den))
            i = j
        
        # Sum all fractions
        result = sum(fractions)
        
        # Convert result to string format
        return f"{result.numerator}/{result.denominator}"