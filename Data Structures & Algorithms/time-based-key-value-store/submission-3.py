class TimeMap:

    def __init__(self):
        self.timeMap = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = [(timestamp,value)]
        else:
            self.timeMap[key].append((timestamp,value))
    def get(self, key: str, timestamp: int) -> str:
        ans = ""
        if key not in self.timeMap:
            return ans
        else:
            L = 0; R = len(self.timeMap[key]) - 1
            while L <= R:
                M = (L+R)//2
                if self.timeMap[key][M][0] <= timestamp:
                    ans = self.timeMap[key][M][1]
                    L = M + 1
                else:
                    R = M - 1
            return ans
        


