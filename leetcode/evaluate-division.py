from collections import deque
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = {}
        for i in range(0, len(values)):
            first = equations[i][0] 
            second = equations[i][1]
            val = values[i]
            
            if first not in graph.keys():
                graph[first] = [(val,second)]
            else:
                graph[first].append((val,second))
            if second not in graph.keys():
                graph[second] = [(1/val, first)]
            else:
                graph[second].append((1/val, first))
        
        def bfs(first,sec):
            queue = deque([(first,1.0)])
            visited = {first}
            while queue:
                cur, rate = queue.popleft()
                if cur == sec:
                    return rate
                else:
                    for val, neighbor in graph[cur]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append((neighbor, val*rate))
            return -1.0
        res = []
        for first, sec in queries:
            if first not in graph.keys() or second not in graph.keys():
                res.append(-1.0)
            else:
                res.append(bfs(first,sec))
        return res