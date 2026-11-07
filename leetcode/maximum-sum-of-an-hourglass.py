class Solution:
    def maxSum(self, grid: list[list[int]]) -> int:
        maxsum = 0
        # for i, j in product(range(1, m), range(1,n)):
        for i in range(1,len(grid)-1):
            for j in range(1,len(grid[i])-1):
                sum_ = (grid[i-1][j-1] + grid[i-1][j] + grid[i-1][j+1]
                            + grid[i][j]+
                        grid[i+1][j-1] + grid[i+1][j] + grid[i+1][j+1])
                if sum_ > maxsum:
                    maxsum = sum_
        return maxsum