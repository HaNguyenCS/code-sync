class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        split = s.split()
        n = len(split)
        count = 0
        for i in split[n-1]:
            count+=1
        return count