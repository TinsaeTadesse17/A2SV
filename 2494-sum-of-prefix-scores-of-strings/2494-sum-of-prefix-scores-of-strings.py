class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]
        self.freq = 1

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:

        root = TrieNode()

        def insert(word):
            curr = root
            for char in word:
                idx = ord(char) - ord('a')
                if not curr.children[idx]:
                    curr.children[idx] = TrieNode()
                else:
                    curr.children[idx].freq += 1
                curr = curr.children[idx]
            curr.is_end = True

        def search(word):
            curr = root
            count = 0
            for char in word:
                idx = ord(char) - ord('a')
                count += curr.children[idx].freq               
                curr = curr.children[idx]
            return count

        for word in words:
            insert(word)
        ans = []
        for word in words:
            ans.append(search(word))
        return ans

        
