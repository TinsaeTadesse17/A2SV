from fractions import Fraction

class Solution:
    def fractionAddition(self, expression: str) -> str:
        if expression[0] != '-':
            expression = '+' + expression
        result = Fraction(0, 1)
        current_number = ""
        for char in expression:
            if char in '+-':
                if current_number:
                    result += Fraction(current_number)
                current_number = char
            else:
                current_number += char
        if current_number:
            result += Fraction(current_number)
        return f"{result.numerator}/{result.denominator}"
