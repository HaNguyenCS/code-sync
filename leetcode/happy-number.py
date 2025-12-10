class Solution:
    def isHappy(self, n: int) -> bool:
        
        s = set()
        if n == 1:
            return True 
        
        while n:
            n = str(n)
            summ = 0
            for digit in n:
                summ = summ + int(digit)**2
            if summ == 1:
                return True
            if summ in s:
                return False
            s.add(summ)
            n = summ