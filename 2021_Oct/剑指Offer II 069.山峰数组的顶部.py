"""
符合下列属性的数组 arr 称为 山峰数组（山脉数组） ：
arr.length >= 3
存在 i（0 < i< arr.length - 1）使得：
arr[0] < arr[1] < ... arr[i-1] < arr[i]
arr[i] > arr[i+1] > ... > arr[arr.length - 1]
给定由整数组成的山峰数组 arr ，返回任何满足
arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
的下标 i，即山峰顶部。
"""
"""
二分法查mid于mid + 1 之间的关系
优化：用两个端点对区间进行三等分，判断两个端点的大小来判断向左还是向右缩进
"""
class Solution:
    def peakIndexInMountainArray(self, arr: list):
        low, high = 0, len(arr) - 1
        while low < high:
            mid = (low + high) // 2
            if arr[mid] < arr[mid + 1]:
                low = mid + 1
            else:
                high = mid
        return high

    def peakIndexInMountainArray2(self, arr: list):
        low, high = 0, len(arr) - 1
        while low < high:
            m1 = low + (high - low) // 3
            m2 = high - (high - low) // 3
            if arr[m1] < arr[m2]:
                low = m1 + 1
            else:
                high = m2 - 1
        return high

s = Solution()
test = [24,69,100,99,79,78,67,36,26,19]
print(s.peakIndexInMountainArray2(test))