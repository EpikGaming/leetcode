import bisect
import collections
class Solution:
    def numSubArrayWithSum(self, nums: list, goal: int):
        presum = [0]
        temp = 0
        for num in nums:
            temp += num
            presum.append(temp)
        hashmap = collections.defaultdict(int, {0: 1})
        res = 0
        for i in range(len(nums)):
            right = presum[i + 1]
            left = right - goal
            res += hashmap[left]
            hashmap[right] += 1
        return res

    def numSubArrayWithSum2(self, nums: list, goal: int):
        res = 0
        l1, l2, s1, s2 = 0, 0, 0, 0
        for i in range(len(nums)):
            s1 += nums[i]
            s2 += nums[i]
            print(s1, s2)
            while l1 <= i and s1 > goal:
                s1 -= nums[l1]
                l1 += 1
                print("test1")
                print(s1)
            while l2 <= i and s2 >= goal:
                s2 -= nums[l2]
                l2 += 1
                print("test2")
                print(s2)
            res += l2 - l1
            print(res, l2, l1)
        return res
test = [1, 0, 0, 0, 1, 0, 1]
s = Solution()
print(s.numSubArrayWithSum(test, 2))
print(s.numSubArrayWithSum2(test, 2))