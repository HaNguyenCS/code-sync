class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        nums = []

        for i in range(1,n+1):
            nums.append(i)
            print(nums)
        sub = []

        def dfs(i):
            if len(sub)>=k:
                res.append(sub.copy())
                return
            if i < len(nums):
                sub.append(nums[i])
                dfs(i+1)
                sub.pop()
                dfs(i+1)
        dfs(0)
        return res