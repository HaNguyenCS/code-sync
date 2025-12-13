class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        sort = {}
        for w in strs:
            s = ''.join(sorted(w))
            if s not in sort:
                sort[s] = [w]
            else:
                sort[s].append(w)
        res = []
        for s in sort.values():
            res.append(s)
        return res