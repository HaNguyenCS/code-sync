from collections import deque
class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:

        adj = [[] for _ in range(n)]
        for flight in flights:
            adj[flight[0]].append((flight[1], flight[2]))
        
        q = deque([(src,0)])
        minsum = [float('inf')] * n
        flightTaken = 0
        while q and flightTaken <= k:
            size = len(q)
            for i in range(size):
                cur,cost = q.popleft()
                for neighbour,price in adj[cur]:
                    if price + cost > minsum[neighbour]:
                        continue
                    minsum[neighbour] = price + cost
                    q.append((neighbour, minsum[neighbour]))
            flightTaken += 1
        return minsum[dst] if minsum[dst] != float('inf') else -1