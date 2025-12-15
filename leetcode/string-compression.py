class Solution:
    def compress(self, chars: List[str]) -> int:
        low = 0
        write = 0
        
        for high in range(len(chars)+1):
            if high == len(chars) or chars[low] != chars[high]:
                chars[write] = chars[low]
                write += 1
                count = high - low
                if count > 1:
                    for c in str(count):
                        chars[write] = c
                        write += 1
                low = high            
        return write