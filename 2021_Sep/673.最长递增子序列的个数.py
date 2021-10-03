class Solution:
    def lengthOfLIS(self, nums: list):
        if not nums:
            return 0
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return dp

    def lengthOfLIS2(self, nums: list):
        if not nums:
            return 0
        stack = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > stack[-1]:
                stack.append(nums[i])
                print(stack)
            else:
                low = 0
                high = len(stack) - 1
                while low <= high:
                    mid = (low + high) // 2
                    if nums[i] > stack[mid]:
                        low = mid + 1
                    else:
                        high = mid - 1
                stack[low] = nums[i]
                print(stack)
        return stack

    def findNumberOfLIS(self, nums: list):
        n, max_len, res = len(nums), 0, 0
        dp = [0] * n
        cnt = [0] * n
        for i, num in enumerate(nums):
            dp[i] = 1
            cnt[i] = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        cnt[i] = cnt[j]
                    elif dp[j] + 1 == dp[i]:
                        cnt[i] += cnt[j]
            if dp[i] > max_len:
                max_len = dp[i]
                res = cnt[i]
            elif dp[i] == max_len:
                res += cnt[i]
        return cnt, res
s = Solution()
test = [10, 9, 2, 5, 3, 7, 101, 18]
print(s.lengthOfLIS(test))
print(s.findNumberOfLIS(test))