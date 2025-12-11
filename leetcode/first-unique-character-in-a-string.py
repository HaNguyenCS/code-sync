class Solution:
    def firstUniqChar(self, s: str) -> int:
        h = {}
        q = deque()
    
        for char in s:
            q.append(char)
            if char not in h.keys():
                h[char] = 1
            else:
                h[char] += 1

        for ind, char in enumerate(list(s)):
            cur = q.popleft()
            if h[cur] == 1:
                return ind
        return -1