class Solution:
    def checkSubarraySum(self, nums: list, k: int):
        nums.insert(0, 0)
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        for i in range(len(nums) - 1, 1, -1):
            for j in range(i - 2, -1, -1):
                if (nums[i] - nums[j]) % k == 0:
                    return True
        return False

    def checkSubarraySum2(self, nums: list, k: int):
        if len(nums) < 2:
            return False
        dic = {0: -1}
        temp = 0
        for i in range(len(nums)):
            temp = (temp + nums[i]) % k
            if temp not in dic:
                dic[temp] = i
            else:
                if i - dic[temp] >= 2:
                    return True
        return False

test = [23, 2, 6, 4, 7]
test2 = [2, 4, 3]
s = Solution()
print(s.checkSubarraySum2(test, 13))
print(s.checkSubarraySum2(test2, 6))