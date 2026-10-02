class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        self.cache = {}
        def dfs(l,r):
            if l > r:
                return 0
            if (l,r) in self.cache:
                return self.cache[(l,r)]
            self.cache[(l,r)] = max(piles[l]-dfs(l+1,r),piles[r]-dfs(l,r-1))
            return self.cache[(l,r)]
        return dfs(0,len(piles)-1) > 0
            
        
        
        