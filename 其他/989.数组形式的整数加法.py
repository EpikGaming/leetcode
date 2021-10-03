class Solution:
    def addToArrayForm(self, A: list, K: int):
        strA = ""
        for i in A:
            strA += str(i)
        result = []
        for i in str(K + int(strA)):
            result.append(int(i))
        return result


s = Solution()
test = [1, 2, 3, 5]
print(s.addToArrayForm(test, 10))