class Solution:
    def encode(self, strs: List[str]) -> str:  
        result = "" 
        for i in strs:
            j = len(i)
            result += f'{j}#{i}'
        print(result)
        return result
    def decode(self, s: str) -> List[str]:
        ans = []
        i =0
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            length = int(s[i:j])
            ans.append(s[j+1:j+1+length])
            i = j + 1 + length
        return ans

                

