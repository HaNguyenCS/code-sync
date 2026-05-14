class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        track = []

        for i in range(0, len(s)):
            if s[i] in track:
                while True:
                    check = track.pop(0)
                    if check == s[i]:
                        break
            track.append(s[i])
            maxlen = max(maxlen,len(track))
        return maxlen