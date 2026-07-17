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
        def dotSearch(curr, i):
            for j in range(i, len(word)):
                if word[j] == '.':
                    if not curr.children:
                        return False
                    else:
                        for k in curr.children.values():
                            if dotSearch(k, j + 1):
                                return True
                        return False
                else:
                    if word[j] not in curr.children:
                        return False
                    curr = curr.children[word[j]]
            return curr.word
        return dotSearch(self.root, 0)
        
