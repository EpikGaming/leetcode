import collections
import sortedcontainers
import bisect
class Solution:
    def getSkyline(self, buildings: list):
        """
        listA = sorted(buildings)
        res = [listA[0][0], listA[0][2]]
        n = len(listA)
        for i in range(1, n):
            prev_left, prev_right, prev_height = listA[i - 1][0], listA[i - 1][1], listA[i - 1][2]
            left, right, height = listA[i][0], listA[i][1], listA[i][2]
            if prev_left < left <= prev_right:
                if height > prev_height:
                    res.append([left, height])
                elif height < prev_height:
                    res.append()
        """

        res = []
        listA = []
        for left, right, height in buildings:
            listA.append((left, -height))
            listA.append((right, height))
        listA.sort()
        prev = 0
        q = sortedcontainers.SortedList([0])              #队列
        for point, height in listA:
            if height < 0:
                q.add(-height)
            else:
                q.remove(height)

            cur = q[-1]
            if cur != prev:
                res.append([point, cur])
                prev = cur
        return res


test = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8], [3, 7, 16], [3, 8, 11], [3, 7, 11]]
s = Solution()
print(s.getSkyline(test))