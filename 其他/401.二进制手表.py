class Solution:
    def readBinaryWatch(self, turnedOn: int):
        res = []
        for i in range(1024):
            h, m = i >> 6, i & 0x3f
            if h < 12 and m < 60 and bin(i).count('1') == turnedOn:
                res.append(f"{h}:{m:02d}")
        return res

    def readBinaryWatch2(self, turnedOn: int):
        res = []
        for i in range(12):
            for j in range(60):
                if bin(i).count('1') + bin(j).count('1') == turnedOn:
                    res.append(f"{i}:{j:02d}")
s = Solution()
print(s.readBinaryWatch(5))