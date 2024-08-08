class Solution:
    def decodeString(self, s: str) -> str:
        idx = []
        temp = []
        
        i = 0
        while i < len(s):
            if s[i].isdigit():
                j = i
                while s[j].isdigit():
                    j += 1
                idx.append(int(s[i:j]))
                i = j
            elif s[i] == "[":
                temp.append("[")
                i += 1
            elif s[i] == "]":
                decoded = ""
                while temp[-1] != "[":
                    decoded = temp.pop() + decoded
                temp.pop()  
                temp.append(decoded * idx.pop())
                i += 1
            else:
                temp.append(s[i])
                i += 1

        return "".join(temp)
