class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        m = len(meetings)
        if m <= n:
            return 0
        meetings.sort(key = lambda x:x[0])
        h = {i:[-1,0] for i in range(n)}
        i = 0
        maxBooked = 0
        room = 0
        while i < m:
            time = meetings[i][0]
            minTime = float('inf')
            foundRoom = False
            for key, val in h.items():
                minTime = min(minTime,val[0])
                if val[0] <= time:
                    val[0] = meetings[i][1]
                    val[1] += 1
                    foundRoom = True
                    break
            if not foundRoom:
                duration = meetings[i][1] - meetings[i][0]
                meetings[i][0] = minTime
                meetings[i][1] = minTime + duration
            else:
                i +=1
        best = -1
        room = 0
        for key in range(n):
            if h[key][1] > best:
                best = h[key][1]
                room = key
        return room
            

                    



        