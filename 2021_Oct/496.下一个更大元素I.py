class Solution:
    def nextGreaterElement(self, nums1: list, nums2: list):
        res = [-1] * len(nums1)
        for i in range(len(nums1)):
            temp = nums2.index(nums1[i])
            if temp == len(nums2):
                continue
            for j in range(temp + 1, len(nums2)):
                if nums2[j] > nums1[i]:
                    res[i] = nums2[j]
                    break
        return res

s = Solution()
test1 = [2, 4]
test2 = [1, 2, 3, 4]
print(s.nextGreaterElement(test1, test2))