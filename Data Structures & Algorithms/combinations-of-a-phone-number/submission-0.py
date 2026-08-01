class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        dial = {"2":"abc","3":"def","4":"ghi","5":"jkl",
        "6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        letters = []
        for digit in digits:
            letters.append(dial[digit])
        ans = []
        def backtrack(i,cur):
            if i == len(letters):
                ans.append(cur[:])
                return 
            for j in range(len(letters[i])):
                cur += letters[i][j]
                backtrack(i+1,cur)
                cur = cur[:-1]
        backtrack(0,"")
        return ans
