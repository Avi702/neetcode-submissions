class Solution:
    import heapq
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i in range(len(tasks)):
            tasks[i].append(i)
        tasks.sort(key=lambda x:x[0])
        tasks = tasks[::-1]
        time = 0
        res = []
        heap = []
        while tasks or heap:
            while tasks and time >= tasks[-1][0]:
                enque, process, index = tasks.pop()
                heapq.heappush(heap,[process,index])
            if heap:
                process, index = heapq.heappop(heap)
                res.append(index)
                time += process
            else:
                time = tasks[-1][0]
        return res

         
            
            
        
                
            
            

