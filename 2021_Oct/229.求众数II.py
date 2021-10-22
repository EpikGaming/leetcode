"""
给定一个大小为 n 的整数数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。
"""
"""
1.哈希表 -> 时间和空间都是O(n)
2.拓展摩尔投票法 -> 时间O(n),空间O(1)
"""
import collections

class Solution:
    def majorityElement(self, nums: list):
        dic = collections.defaultdict(int)
        res = []
        for num in nums:
            dic[num] += 1
        for key, value in dic.items():
            if value > len(nums) // 3:
                res.append(key)
        return res

    def majorityElement2(self, nums: list):
        res = []
        element1, element2 = 0, 0
        vote1, vote2 = 0, 0
        for num in nums:
            if vote1 > 0 and num == element1:
                vote1 += 1
            elif vote2 > 0 and num == element2:
                vote2 += 1
            elif vote1 == 0:
                element1 = num
                vote1 += 1
            elif vote2 == 0:
                element2 = num
                vote2 += 1
            else:
                vote1 -= 1
                vote2 -= 1
        cnt1, cnt2 = 0, 0
        for num in nums:
            if vote1 > 0 and num == element1:
                cnt1 += 1
            if vote2 > 0 and num == element2:
                cnt2 += 1
        if vote1 > 0 and cnt1 > len(nums) // 3:
            res.append(element1)
        if vote2 > 0 and cnt2 > len(nums) // 3:
            res.append(element2)
        return res


s = Solution()
test = [1, 2, 3, 1, 2, 3, 1, 2]
print(s.majorityElement2(test))