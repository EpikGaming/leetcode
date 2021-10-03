class Solution:
    def findUnsortedSubarray(self, nums: list):
        n = len(nums)
        maxn, right = float('-inf'), -1
        minn, left = float('inf'), -1

        for i in range(n):
            if nums[i] >= maxn:
                maxn = nums[i]
            else:
                right = i

            if nums[n - i - 1] <= minn:
                minn = nums[n - i - 1]
            else:
                left = n - i - 1
            print(left, right, minn, maxn)

        return 0 if right == -1 else right - left + 1

s = Solution()
test = [1,4,8,10,6,7,8]
print(s.findUnsortedSubarray(test))