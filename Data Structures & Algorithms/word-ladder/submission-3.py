class Solution:
    from collections import deque, defaultdict
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        n = len(beginWord)
        def checkDiff(word1,word2):
            diff = 0
            for i in range(n):
                if word1[i] != word2[i]:
                    diff += 1
            return diff
    
        graph = defaultdict(list)
        wordList.append(beginWord)
        for word1 in wordList:
            for word2 in wordList:
                if word1 == word2:
                    continue
                elif checkDiff(word1,word2) == 1:
                    graph[word1].append(word2)
                    graph[word2].append(word1)
        q = deque()
        q.append(beginWord)
        visit = set()
        visit.add(beginWord)
        step = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return step
                for nei in graph[word]:
                    if nei not in visit:
                        q.append(nei)
                        visit.add(nei)
            step += 1
        return 0

        