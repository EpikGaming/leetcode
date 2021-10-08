"""
所有 DNA 都由一系列缩写为 'A'，'C'，'G' 和 'T' 的核苷酸组成，
例如："ACGAATTCCG"。在研究 DNA 时，识别 DNA 中的重复序列有时会对研究非常有帮助。
编写一个函数来找出所有目标子串，目标子串的长度为 10，且在 DNA 字符串 s 中出现次数超过一次。
"""
"""
目标子串长度固定为10 -> 滑动窗口
且超过一次就行 -> if dic[str] == 2
字符串只由4个字符组成:"A" "C" "G" "T"，二进制排列
令"A" -> 00 ; "C" -> 01 ; "G" -> "10" ; "T" -> "11"
"""
import collections
class Solution:
    def findRepeatedDnaSequences(self, s: str):
        L = 10
        temp = {"A": 0, "C": 1, "G": 2, "T": 3}
        res = []
        n = len(s)
        #字符串长度不足10情况，返回空数组[]
        if n <= L:
            return res
        x = 0
        dic = collections.defaultdict(int)
        #先记录前9个
        for ch in s[:L - 1]:
            #print(ch)
            x = (x << 2) | temp[ch]
            #print(x)
        for i in range(n - L + 1):
            #print(i)
            #1.滑动窗口向右移动一个字符位，即x向右移动两个比特位 x = x << 2
            #2.新字符串进入窗口 x | temp[s[j]] ;i = 0,1,2... -> j = 9,10,11 -> j = i + 10(L) - 1
            #3.滑动窗口最左字符弹出，即保留x 20个比特位 x = x | (0b11111111111111111111)
            #表示成 1右移20位-1  100000000000000000000 - 1 -> (1 << 20(2 * L)) - 1
            x = ((x << 2) | temp[s[i + L - 1]]) & ((1 << (L * 2)) - 1)
            #print(bin(x))
            dic[x] += 1
            #哈希表统计，边计数边放入结果
            if dic[x] == 2:
                res.append(s[i: i + 10])
        print(dic)
        return res

    #朴素哈希表
    def findRepeatedDnaSequences2(self, s: str):
        L = 10
        res = []
        dic = collections.defaultdict(int)
        for i in range(len(s) - L + 1):
            x = s[i:i + L]
            dic[x] += 1
            if dic[x] == 2:
                res.append(x)
        return res

s = Solution()
test = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print(s.findRepeatedDnaSequences2(test))