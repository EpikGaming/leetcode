import bisect
class Solution:
    def lengthOfLIS(self, nums: list):
        n = len(nums)
        dp = [float("inf")] * n
        res = 1
        dp[0] = nums[0]
        for i in range(1, n):
            if nums[i] > dp[res - 1]:
                dp[res] = nums[i]
                res += 1
            else:
                print(bisect.bisect_left(dp, nums[i]))
                dp[bisect.bisect_left(dp, nums[i])] = nums[i]
            print(dp)
        return dp, res

s = Solution()
test = [6,3,5,10,11,2,9,14,13,7,4,8,12]
print(s.lengthOfLIS(test))