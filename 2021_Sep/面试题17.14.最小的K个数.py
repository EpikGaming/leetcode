import heapq
class Solution:
    def smallestK(self, arr: list, k: int):
        if k == 0:
            return []
        hp = [-x for x in arr[:k]]
        heapq.heapify(hp)
        for i in range(k, len(arr)):
            if -arr[i] > hp[0]:
                heapq.heappop(hp)
                heapq.heappush(hp, -arr[i])
        return [-x for x in hp]


s = Solution()
test = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
print(s.smallestK(test, 4))