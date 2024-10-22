class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        for c in expression:
            if c!=')' and c!=',':
                stack.append(c)
            elif c==')':
                exp = []
                while stack and stack[-1]!='(':
                    t = stack.pop()
                    exp.append(True if t=='t' else False)

                stack.pop()
                if stack:
                    op = stack.pop()
                    v = exp[0]
                    if op=='&':
                        for i in exp:
                            v = v&i
                    elif op=='|':
                        for i in exp:
                            v=v|i
                    else:
                        v = not v
                    stack.append('t' if v else 'f')
            print(stack)
        return stack[-1]=='t'


        