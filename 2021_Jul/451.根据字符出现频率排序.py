import collections
import heapq
class Solution:
    def frequencySort(self, s: str):
        dic = collections.defaultdict(int)
        for c in s:
            dic[c] += 1
        hq = []
        for k, v in dic.items():
            heapq.heappush(hq, (-v, ord(k), k))
        print(hq)
        res = []
        while hq:
            num, _, char = heapq.heappop(hq)
            res.append(char * (-num))
        return res

s = Solution()
test = "Aabb"
print(s.frequencySort(test))