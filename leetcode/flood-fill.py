class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        q = deque()
        q.append((sr,sc))
        org = image[sr][sc]
        if color == org:
            return image

        while q:
            sr,sc = q.popleft()
            cur = image[sr][sc]
            # image[sr-1][sc]
            # image[sr][sc-1]
            # image[sr+1][sc]
            # image[sr][sc+1]
            if cur == org:
                image[sr][sc] = color
                if 0<=sr-1<rows and 0<=sc<cols:
                    q.append((sr-1,sc))
                if 0<=sr<rows and 0<=sc-1<cols:
                    q.append((sr,sc-1))
                if 0<=sr+1<rows and 0<=sc<cols:
                    q.append((sr+1,sc))
                if 0<=sr<rows and 0<=sc+1<cols:
                    q.append((sr,sc+1))
        
        return image