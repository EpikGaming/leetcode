class Solution:
    def numberOfArithmeticSlices(self, nums: list):
        n = len(nums)
        if n < 3:
            return 0
        combo = 0
        res = 0
        for i in range(2, n):
            if nums[i - 2] - nums[i - 1] == nums[i - 1] - nums[i]:
                combo += 1
            else:
                res += (combo + 1) * combo // 2
                combo = 0
        res += (combo + 1) * combo // 2
        return res

s = Solution()
test = [5,4,3,2,1,0,-1]
print(s.numberOfArithmeticSlices(test))