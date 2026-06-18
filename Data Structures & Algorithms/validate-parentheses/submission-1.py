class Solution:
    def isValid(self, s: str) -> bool:
        h = {']':'[','}':'{',')':'('}
        stack = []
        for i in s:
            if i == '[' or i == '{' or i =='(':
                stack.append(i)
            elif stack and h[i] == stack[-1]:
                stack.pop()
            else:
                return False
        print(stack)
        if stack:
            return False
        return True
            
            
