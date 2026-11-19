from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        
        adj = [[] for _ in range(numCourses)]
        degree = [0] * numCourses

        for course, pre in prerequisites:
            degree[course] += 1
            adj[pre].append(course)

        q = deque([i for i in range(numCourses) if degree[i]==0])
        count = 0
        while q:
            cur = q.popleft()
            count += 1
            for neighbour in adj[cur]:
                degree[neighbour] -= 1
                if degree[neighbour] == 0:
                    q.append(neighbour)

        return count == numCourses