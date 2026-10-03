class TrieNode:
    def __init__(self):
        self.children = {}
        self.endWord = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endWord = True
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        m = len(board)
        n = len(board[0])
        self.res = []
        def dfs(r,c,visit,word,node):
            if r >= m or c >= n or r < 0 or c < 0 or (r,c) in visit or board[r][c] not in node.children:
                return
            word.append(board[r][c])
            visit.add((r,c))
            temp = node.children[board[r][c]]
            if temp.endWord:
                self.res.append("".join(word))
                temp.endWord = False
            dfs(r+1,c,visit,word,node.children[board[r][c]])
            dfs(r-1,c,visit,word,node.children[board[r][c]])
            dfs(r,c+1,visit,word,node.children[board[r][c]])
            dfs(r,c-1,visit,word,node.children[board[r][c]])
            visit.remove((r,c))
            word.pop()
        for r in range(m):
            for c in range(n):
                dfs(r,c,set(),[],trie.root)
        return self.res

        