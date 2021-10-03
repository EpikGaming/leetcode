class Solution:
    def reverseVowels(self, s: str):
        temp = ["a", "e", "i", "o", "u"]
        i, j = 0, len(s) - 1
        res = list(s)
        while i < j:
            if res[i] in temp:
                if res[j] in temp:
                    res[i], res[j] = res[j], res[i]
                    i += 1
                    j -= 1
                else:
                    j -= 1
            else:
                if res[j] in temp:
                    i += 1
                else:
                    i += 1
                    j -= 1
        return "".join(res)

test = "hellllllll"
s= Solution()
print(s.reverseVowels(test))