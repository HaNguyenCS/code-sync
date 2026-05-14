class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_len = 0
        count = {}
        max_freq = 0
        
        for h in range(len(s)):
            count[s[h]] = 1 + count.get(s[h],0)
            window_len = h-l+1
            max_freq = max(max_freq, count[s[h]])
            if window_len - max_freq > k:
                count[s[l]] -= 1
                l += 1
            else:
                max_len = max(max_len, window_len)

        return max_len