class Solution:
    def checkValidString(self, s: str) -> bool:
        self.cache = {}
        def dfs(i,bal):
            if bal < 0:
                return False
            if i == len(s):
                return bal == 0
            if (i, bal) in self.cache:
                return self.cache[(i,bal)]
            if s[i] == "*":
                self.cache[(i,bal)] = dfs(i+1,bal-1) or dfs(i+1,bal+1) or dfs(i+1,bal)
            elif s[i] == '(':
                self.cache[(i,bal)] = dfs(i+1,bal+1)
            else:
                self.cache[(i,bal)] = dfs(i+1,bal-1)
            return self.cache[(i,bal)]
        return dfs(0,0)
                
                    


