class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for ind,val in enumerate(temperatures):
            if len(stack) == 0:
                stack.append((ind, val))
            else:
                while stack and stack[-1][1] < val:
                    index,_ = stack.pop()
                    res[index] = ind - index
                stack.append((ind,val))
        return res
                
                    

                    

        if len(res) < len(stack):
            i = 0
            while i < (len(stack) - len(res)):
                res.append(0)
        return res