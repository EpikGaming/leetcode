import random
class Solution:
    def rand7(self):
        return random.randint(1, 7)

    def rand10(self):
        while True:
            row = self.rand7()
            col = self.rand7()
            idx = (row - 1) * 7 + col
            print(idx)
            if idx <= 40:
                return 1 + (idx - 1) % 10
s = Solution()
print(s.rand10())