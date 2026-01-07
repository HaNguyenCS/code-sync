class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # either 1 or 2 steps
        # start at 0 -> cost[0] = sum[0]
        # start at 1 -> cost[1] = sum[1]
        # at step n -> min(cost[n] + sum[n-1], cost[n] + sum[n-2]
        for c in cost[2:]:
            temp = min(c + cost[0], c + cost[1])
            cost[0] = cost[1]
            cost[1] = temp
        return min(cost[0], cost[1])