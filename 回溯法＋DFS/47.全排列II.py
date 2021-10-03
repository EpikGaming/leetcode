class Solution:
    def permuteUnique(self, nums: list):
        res = []
        n = len(nums)

        def dfs(x: int):
            if x == n - 1:
                res.append(nums[:])

            dic = set()
            for i in range(x, n):
                if nums[i] in dic:
                    continue
                dic.add(nums[i])
                nums[i], nums[x] = nums[x], nums[i]
                dfs(x + 1)
                nums[i], nums[x] = nums[x], nums[i]

        dfs(0)
        return res

s = Solution()
test = ['a', 'b', 'b']
print(s.permuteUnique(test))