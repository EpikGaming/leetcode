class Solution:
    def findPeakElement(self, nums: list):
        n = len(nums)
        if n == 1:
            return 0
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return right

s = Solution()
test = [1, 2, 3, 1]
print(s.findPeakElement(test))