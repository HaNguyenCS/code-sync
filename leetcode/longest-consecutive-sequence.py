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