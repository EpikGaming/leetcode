class Solution:
    def numRescueBoats(self, people: list, limit: int):
        res = 0

        def quick_sort(array: list, left: int, right: int):
            if left >= right:
                return
            i, j = left, right
            while i < j:
                while i < j and array[j] >= array[left]:
                    j -= 1
                while i < j and array[i] < array[left]:
                    i += 1
                array[i], array[j] = array[j], array[i]
            array[left], array[i] = array[i], array[left]
            quick_sort(array, left, i - 1)
            quick_sort(array, i + 1, right)
            return array
        people = quick_sort(people, 0, len(people) - 1)
        i, j = 0, len(people) - 1
        while i <= j:
            if people[i] + people[j] > limit:
                j -= 1
            else:
                i += 1
                j -= 1
            res += 1
        return res

s = Solution()
test = [3, 2, 2, 1]
print(s.numRescueBoats(test, 3))