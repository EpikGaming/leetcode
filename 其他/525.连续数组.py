class Solution:
    def findMaxLength(self, nums: list):
        dic = {0: -1}
        temp = res = 0
        for i in range(len(nums)):
            temp += 1 if nums[i] == 1 else -1
            if temp in dic:
                res = max(res, i - dic[temp])
            else:
                dic[temp] = i
        return res

s = Solution()
test = [0,1,0,1,0,0,1]
print(s.findMaxLength(test))