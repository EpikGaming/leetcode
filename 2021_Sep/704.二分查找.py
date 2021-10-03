class Solution:
    def search(self, nums: list, target: int):
        i, j = 0, len(nums) - 1
        while i <= j:
            mid = (j - i) // 2 + i
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                j = mid - 1
            else:
                i = mid + 1
        return -1


s = Solution()
test = [-1, 0, 3, 5, 9, 12]
print(s.search(test, 5))