class Solution:
    def canPartitionKSubsets(self, nums: list, k: int):
        n = len(nums)
        if k > n or sum(nums) % k != 0:
            return False
        bucket = [0] * k
        target = sum(nums) / k
        nums.sort(reverse=True)
        print(nums)

        def traceback(arr: list, index: int, buckets: list, targets: int):
            if index == n:
                for i in range(len(buckets)):
                    if buckets[i] != targets:
                        return False

                return True

            for i in range(len(buckets)):
                if buckets[i] + arr[index] > targets:
                    continue
                buckets[i] += arr[index]
                if traceback(arr, index + 1, buckets, targets):
                    return True
                buckets[i] -= arr[index]
            return False
        return traceback(nums, 0, bucket, target)

    def canPartitionKSubsets2(self, nums: list, k: int):
        if k > len(nums) or sum(nums) % k != 0:
            return False

        target = sum(nums) / k
        num_used = [False for _ in range(len(nums))]

        def traceback(n: int, now_sum: int, arr: list, start: int, used: list, targets: int):
            if n == 0:
                return True

            if now_sum == targets:
                print(n)
                return traceback(n - 1, 0, arr, 0, used, targets)

            for i in range(start, len(arr)):
                if used[i] or now_sum + arr[i] > targets:
                    continue
                used[i] = True
                now_sum += arr[i]
                print(used)
                if traceback(n, now_sum, arr, i + 1, used, targets):
                    return True
                used[i] = False
                now_sum -= arr[i]
                print(used)
            return False
        return traceback(k, 0, nums, 0, num_used, target)

s = Solution()
test = [4, 3, 2, 3, 5, 2, 1]
#print(s.canPartitionKSubsets(test, 4))
print(s.canPartitionKSubsets2(test, 4))