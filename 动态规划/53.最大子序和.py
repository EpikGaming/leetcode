class Solution:
    def maxSubArray(self, nums: list):
        #朴素dp
        n = len(nums)
        dp = [float("-inf")] * n
        dp[0] = res = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            res = max(res, dp[i])
        return res

    def maxSubArray2(self, nums: list):
        #压缩存储空间，因为dp[i]只跟dp[i - 1]有关
        n = len(nums)
        a = nums[0]
        if n == 1:
            return a
        b = max(nums[1], nums[0] + nums[1])
        res = max(a, b)
        for i in range(2, n):
            if b >= 0:                  #如果b > 0,说明b的贡献为正，可以加入nums[i]中
                a, b = b, b + nums[i]
                res = max(res, b)       #打个tag，看看是不是最大值
            else:
                a, b = b, nums[i]       #如果b < 0,说明b的贡献为负，不能加入
                res = max(res, b)       #查看单个数组元素是否是最大值
        return res

s = Solution()
test = [-2,1,-3,4,-1,2,1,-5,4]
print(s.maxSubArray(test))
print(s.maxSubArray2(test))
