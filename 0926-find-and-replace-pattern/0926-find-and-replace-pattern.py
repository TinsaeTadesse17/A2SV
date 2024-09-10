class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        for word in words:
            hashmap = {}
            hashmap2 = {}
            flag = True
            for idx,char in enumerate(word):
                if char in hashmap:
                    if hashmap[char] != pattern[idx]:
                        flag = False
                elif pattern[idx] in hashmap2:
                    if hashmap2[pattern[idx]] != char:
                        flag = False
                else:
                    hashmap[char] = pattern[idx]
                    hashmap2[pattern[idx]] = char
            if flag:
                ans.append(word)
        return ans

