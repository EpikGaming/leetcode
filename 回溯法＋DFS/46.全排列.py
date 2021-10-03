class Solution:
    def permute(self, nums: list):
        n = len(nums)
        res = []

        def dfs(x):
            if x == n - 1:
                res.append(nums[:])
                return

            for i in range(x, n):
                nums[x], nums[i] = nums[i], nums[x]
                dfs(x + 1)
                nums[x], nums[i] = nums[i], nums[x]

        dfs(0)
        return res

s = Solution()
test = [1, 2, 3, 4]
print(s.permute(test))