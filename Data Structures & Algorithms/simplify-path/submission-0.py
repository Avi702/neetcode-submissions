class Solution:
    def simplifyPath(self, path: str) -> str:
        #["neetcode","practice","","...","","","..","courses"]
        """
        "" or ".."   append to our stack. 
        stack = ["neetcode","practice","courses"]
        """
        stack = []
        for i in path.split("/"):
            if i == "" or i == ".":
                continue
            if stack and i == "..":
                stack.pop()
            elif i != "..":
                stack.append(i)
        return "/"+ "/".join(stack)