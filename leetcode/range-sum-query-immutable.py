class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix = [0] * (1+len(self.nums))
        self.prefix[1] = self.nums[0]
        for i, val in enumerate(nums):
            self.prefix[i + 1] = self.prefix[i] + val

    def sumRange(self, left: int, right: int) -> int:
        # return sum(self.nums[left:right+1])
        return self.prefix[right+1]-self.prefix[left]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)