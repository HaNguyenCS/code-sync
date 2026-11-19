import heapq
from collections import Counter
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        freq = Counter(tasks)

        maxheap = [(-count,task) for task, count in freq.items()]
        heapq.heapify(maxheap)

        # res = []
        interval = 0
        while maxheap:
            wait = []
            execute = 0 
            for _ in range(n+1):
                if not maxheap:
                    break
                count, task = heapq.heappop(maxheap)
                count+=1
                execute += 1
                if count < 0:
                    wait.append((count,task))
            
            for c,t in wait:
                heapq.heappush(maxheap, (c,t))
            interval += n+1 if maxheap else execute
        return interval