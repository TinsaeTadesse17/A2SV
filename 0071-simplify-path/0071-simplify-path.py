class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = ["/"]

        files = path.split("/")
        for char in files:
            if char:
                if char == "..":
                    if len(stack) > 1:
                        for i in range(2):
                            stack.pop()
                    else:
                        continue

                elif char == ".":
                    continue

                else:
                    stack.append(char)
                    stack.append("/")

        if len(stack) > 1 and stack[-1] =="/":
            stack.pop()

        return "".join(stack)



























        # for i,char in enumerate(path):
        #     if not stack and char == "/":
        #         stack.append(char)
        #     elif stack and char == "/" and (stack[-1] == "/" or i == n-1 ):
        #         continue
        #     elif stack and stack[-1] == ".":
        #         if char == ".":
        #             if (i == 1 or (i > 1 and path[i-2] != ".")) and ((i < n-1 and path[i + 1] != ".") or i == n-1):
        #                 if i == 1:
        #                     stack.pop()
        #                 else:
        #                     for i in range(2):
        #                         stack.pop()
        #                 while stack and stack[-1] != "/":
        #                     stack.pop()
        #             else:
        #                 stack.append(char)    
        #         else:
        #             stack.pop()
        #             if char != "/":
        #                 stack.append(char)
        #     elif stack:
        #         stack.append(char)

        # return "".join(stack)
