class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end = True

    def longest_common_prefix(self, word: str) -> int:
        curr = self.root
        length = 0
        for char in word:
            if char in curr.children:
                curr = curr.children[char]
                length += 1
            else:
                break
        return length

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = Trie()
        #add arr1
        for num in arr1:
            trie.insert(str(num))
        #find common prefix in arr2
        max_length = 0
        for num in arr2:
            max_length = max(max_length, trie.longest_common_prefix(str(num)))
        
        return max_length

