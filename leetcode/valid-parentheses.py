class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        l = {'(':')', '{':'}', '[':']'}
        for i in s:
            if i in l.keys():
                stack.append(i)
            else:
                if len(stack) != 0:
                    key = stack.pop()
                    if i != l[key]:
                        return False
                else:
                    return False
        if len(stack) == 0:
            return True
        return False