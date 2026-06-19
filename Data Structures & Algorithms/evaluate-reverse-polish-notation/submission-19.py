class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for i in tokens:
            total = 0
            if i == "+":
                total = s[-1]
                s.pop()
                total += s[-1]
                s.pop()
                s.append(total)
            elif i == "-":
                total = s[-1]
                s.pop()
                total = s[-1] - total
                s.pop()
                s.append(total)
            elif i == "*":
                total = s[-1]
                s.pop()
                total = total * s[-1]
                s.pop()
                s.append(total)
            elif i == "/":
                total = s[-1]
                s.pop()
                total = int(s[-1] / total)
                s.pop()
                s.append(total)
            else:
                s.append(int(i))
        return s[-1]

