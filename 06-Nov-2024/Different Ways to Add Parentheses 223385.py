# Problem: Different Ways to Add Parentheses - https://leetcode.com/problems/different-ways-to-add-parentheses/

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        @cache
        def compute(expression):
            if expression.isdigit():
                return [int(expression)]
            
            results = []
            for i, char in enumerate(expression):
                if char in "+-*":
                    left_res = compute(expression[:i])
                    right_res = compute(expression[i+1:])
                    
                    for left in left_res:
                        for right in right_res:
                            if char == '+':
                                results.append(left + right)
                            elif char == '-':
                                results.append(left - right)
                            elif char == '*':
                                results.append(left * right)
            
            return results
        
        return compute(expression)

