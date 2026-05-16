class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        track = {}
        max_len =0 

        for num in nums:
            if num in track:
                continue
            
            l = track.get(num-1,0)
            r = track.get(num+1,0)

            length = l + 1 + r
            track[num] = length
            
            track[num-l] = length
            track[num+r] = length

            max_len = max(max_len, length)
        return max_len

# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         nums_set = set(nums)
#         longest = 0

#         for num in nums_set:
#             # Only start counting if num is the beginning of a sequence
#             if num - 1 not in nums_set:
#                 current = num
#                 length = 1

#                 while current + 1 in nums_set:
#                     current += 1
#                     length += 1

#                 longest = max(longest, length)

#         return longest