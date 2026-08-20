class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timeMap:
            self.timeMap[key].append((value,timestamp))
            return
        self.timeMap[key] = [(value,timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        n = self.timeMap[key]
        L = 0
        R = len(n) - 1
        maxval = ""
        index = 0
        while L <= R:
            M = (L+R)//2
            if n[M][1] > timestamp:
                R = M - 1
            elif n[M][1] <= timestamp:
                maxval = n[M][0]
                L = M + 1
        return maxval
        
