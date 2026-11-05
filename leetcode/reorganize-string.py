import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = {}

        for char in s:
            freq[char] = freq.get(char,0)+1
        
        max_heap = []
        for char, val in freq.items():
            max_heap.append((-val, char))
        
        heapq.heapify(max_heap)
        res = []
        while len(max_heap) >= 2:
            freq1, char1 = heapq.heappop(max_heap)
            freq2, char2 = heapq.heappop(max_heap)
            res.extend([char1,char2])

            if freq1+1<0:
                heapq.heappush(max_heap, (freq1+1,char1))
            if freq2+1<0:
                heapq.heappush(max_heap, (freq2+1,char2))
        
        if max_heap:
            freq,char = heapq.heappop(max_heap)
            res.append(char)
            freq+=1
            if freq<0:
                return ""

        return "".join(res)