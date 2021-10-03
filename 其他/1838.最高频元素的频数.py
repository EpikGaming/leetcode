class Solution:
    def maxFrequency(self, nums: list, k: int):
        nums.sort()
        n = len(nums)
        left = 0
        res = 1
        total = 0
        for right in range(1, n):
            total += (right - left) * (nums[right] - nums[right - 1])
            while total > k:
                total += nums[left] - nums[right]
                left += 1
            res = max(res, right - left + 1)
        return res

s = Solution()
test = [1, 2, 4]
print(s.maxFrequency(test, 5))