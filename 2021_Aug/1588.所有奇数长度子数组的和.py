class Solution:
    def sumOddLengthSubArray(self, arr: list):
        temp = 1
        res = 0
        arr = [0] + arr
        for i in range(1, len(arr)):
            arr[i] += arr[i - 1]
        while temp < len(arr):
            for j in range(temp, len(arr)):
                res += arr[j] - arr[j - temp]
            temp += 2
        return res


s = Solution()
test = [1, 4, 2, 5]
print(s.sumOddLengthSubArray(test))