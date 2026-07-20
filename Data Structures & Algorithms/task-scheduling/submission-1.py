class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import deque
        h = {}
        for i in range(len(tasks)):
            if tasks[i] not in h:
                h[tasks[i]] = 1
            else:
                h[tasks[i]] += 1
        task = []
        for val in h.values():
            task.append(-val)
        import heapq
        heapq.heapify(task)
        q = deque()
        time = 0
        while q or task:
            if q and q[0][-1] == time:
                heapq.heappush(task,q.popleft()[0])
            if task:
                count = heapq.heappop(task) + 1
                if count < 0:
                    q.append((count, time + n + 1))
            time += 1
            
        return time
            

            
            


                
