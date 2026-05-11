class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""

        root = Trie()
        for word in strs:
            root.insert(word)
        
        # traverse to find longest -> until more than one child
        node = root.root
        while len(node.children) == 1 and not node.is_end:
            char = list(node.children.keys())[0]
            ans += char
            node = node.children[char]

        return ans
            