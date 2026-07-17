class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True
        

    def search(self, word: str) -> bool:
        def dfs(curr, i):
            for j in range(i, len(word)):
                if word[j] == '.':
                    for c in curr.children.values():
                        if dfs(c, j + 1):
                            return True
                    return False
                else:
                    if word[j] not in curr.children:
                        return False
                    curr = curr.children[word[j]]
            return curr.word
        return dfs(self.root, 0)
        
