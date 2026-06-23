class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s = []
        for i in operations:
            if i == "+":
                score1 = s[-1]
                score2 = s[-2]
                s.append(score1+score2)
            elif i == "D":
                score = s[-1]
                s.append(score*2)
            elif i == "C":
                s.pop()
            else:
                s.append(int(i))
            print(s)
        return sum(s)