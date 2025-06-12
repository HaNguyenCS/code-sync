class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = -inf
        l = 0
        
        for r in range(1, len(nums)):
            
            while total < total + nums[r]:
                total = total + nums[r]