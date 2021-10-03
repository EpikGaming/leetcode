class Solution:
    def maxIceCream(self, costs: list, coins: int):
        costs.sort()
        sumCount = 0
        i = 0
        for i in range(len(costs)):
            sumCount += costs[i]
            if sumCount > coins:
                break
            i += 1
        return i


s = Solution()
iceCream = [10, 6, 8, 9, 11]
print(s.maxIceCream(iceCream, 5))