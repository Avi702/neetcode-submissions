class Solution:
    from collections import Counter, deque
    import heapq
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        k = Counter(tasks)
        task = []
        for key, val in k.items():
            task.append([-val,0,key])
        heapq.heapify(task)
        q = deque()
        while task or q:
            if q and q[0][1] == time:
                count, nextCycle, func = q.popleft()
                heapq.heappush(task,[count,nextCycle,func])
            if task:
                count, nextCycle, func = heapq.heappop(task)
                if count < -1:
                    q.append([count+1,time+n+1,func])
            time += 1
        return time
