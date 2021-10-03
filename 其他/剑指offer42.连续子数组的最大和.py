class Solution:
    def maxSubArray(self, nums: list):
        a = nums[0]
        b = max(nums[1], nums[0] + nums[1])
        res = max(a, b)
        print(a, b)
        for i in range(2, len(nums)):
            if b >= 0:
                a, b = b, b + nums[i]
                print(a, b)
                res = max(res, b)
                print(res, 1111)
            else:
                a, b = b, nums[i]
                print(a, b)
                res = max(res, b)
                print(res, 2222)

        return res

s = Solution()
test = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
test = [-2, 1]
print(s.maxSubArray(test))