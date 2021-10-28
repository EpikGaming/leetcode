def isPowerOf2(n: int):
    return (n & (n - 1)) == 0

class Solution:
    def reorderedPowerOf2(self, n: int):
        nums = sorted(list(str(n)))
        m = len(nums)
        visited = [False] * m

        def traceback(idx: int, num: int):
            print(visited, idx, num)
            if idx == m:
                return isPowerOf2(num)

            for i, ch in enumerate(nums):
                print(i, ch)
                if (num == 0 and ch == "0") or visited[i] or (i > 0 and not visited[i - 1] and ch == nums[i - 1]):
                    continue
                visited[i] = True

                if traceback(idx + 1, num * 10 + ord(ch) - ord("0")):
                    return True

                visited[i] = False

            return False
        return traceback(0, 0)

s = Solution()
print(s.reorderedPowerOf2(1))