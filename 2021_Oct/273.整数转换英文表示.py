singles = ["", "One", "Two", "Three", "Four",
           "Five", "Six", "Seven", "Eight", "Nine"]
teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen",
         "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
tens = ["", "Ten", "Twenty", "Thirty", "Forty",
        "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
thousands = ["", "Thousand", "Million", "Billion"]

class Solution:
    def numberToWords(self, num: int):
        if num == 0:
            return "Zero"

        def recursion(x: int):
            s = ""
            if x == 0:
                return s
            elif x < 10:
                s += singles[x] + " "
            elif x < 20:
                s += teens[x - 10] + " "
            elif x < 100:
                s += tens[x // 10] + " " + recursion(x % 10)
            else:
                s += singles[x // 100] + " Hundred " + recursion(x % 100)
            return s

        s = ""
        unit = int(1e9)
        for i in range(3, -1, -1):
            curNum = num // unit
            if curNum:
                num -= curNum * unit
                s += recursion(curNum) + thousands[i] + " "
            unit //= 1000
        return s.strip()

s = Solution()
test = 1234567
print(s.numberToWords(test))