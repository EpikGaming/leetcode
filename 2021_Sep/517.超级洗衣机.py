class Solution:
    def findMinMoves(self, machines: list):
        n = len(machines)
        s = sum(machines)
        if s % n != 0:
            return -1
        per = s // n
        for i in range(n):
            machines[i] -= per
        cur_sum = max_sum = res = 0
        for m in machines:
            cur_sum += m
            max_sum = max(max_sum, abs(cur_sum))
            res = max(res, max_sum, m)
            print(cur_sum, max_sum, res)
        return res

s = Solution()
test = [1, 0, 5]
print(s.findMinMoves(test))