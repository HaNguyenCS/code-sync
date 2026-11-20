from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        adj = [[] for _ in range(numCourses)]
        preq = [0] * numCourses
        for course, pre_course in prerequisites:
            adj[pre_course].append(course)
            preq[course] += 1
        
        q = deque()
        for i in range(len(preq)):
            if preq[i] == 0:
                q.append(i)

        res = []
        while q:
            cur = q.popleft()
            res.append(cur)
            for neighbour in adj[cur]:
                preq[neighbour] -= 1
                if preq[neighbour] == 0:
                    q.append(neighbour)
        
        print(res)
        if len(res) == numCourses:
            return res
        return []