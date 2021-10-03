class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: list):
        arr.sort()
        dic = {}
        res = 1
        for i in range(len(arr)):
            if arr[i] not in dic:
                dic[res] = arr[i]
                res += 1
        return dic

s = Solution()
test = [1, 100, 100, 2, 3, 2]
print(s.maximumElementAfterDecrementingAndRearranging(test))