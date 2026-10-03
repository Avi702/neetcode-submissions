class TrieNode:
    def __init__(self):
        self.children = {}
        self.endWord = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endWord = True
    def search(self, word: str) -> bool:
        cur = self.root
        n = len(word)
        def dfs(root,i):
            if i == n:
                return root.endWord
            if word[i] == ".":
                for c in root.children:
                    res = dfs(root.children[c],i+1)
                    if res:
                        return res
            if word[i] in root.children:
                return dfs(root.children[word[i]],i+1)
            return False
        return dfs(cur,0)
                

        
