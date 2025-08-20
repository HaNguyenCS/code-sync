class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        target = tickets[k]
        
        for ind, val in enumerate(tickets):
            if ind <= k:
                time = time + min(val, target)
            else:
                time = time + min(val, target - 1)
        return time