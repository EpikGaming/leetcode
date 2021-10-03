class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next = None

class Solution:
    def splitListToParts(self, head: ListNode, k: int):
        n = 0
        temp = head
        while temp:
            n += 1
            temp = temp.next
        x, y, i = n // k, n % k, 0
        res = [None] * k
        cur = head
        while i < k and cur is not None:
            res[i] = cur
            size = x + (1 if i < y else 0)
            for j in range(1, size):
                cur = cur.next
            print(cur.val)
            temp = cur.next
            cur.next = None
            cur = temp
            i += 1
        for link in res:
            if link:
                n = 0
                print("head", link.val)
                while link:
                    n += 1
                    link = link.next
                print("length", n)
            else:
                print('[]')

        return res


s = Solution()
test = ListNode(1)
dummy = test
for i in range(2, 11):
    dummy.next = ListNode(i)
    dummy = dummy.next
print(s.splitListToParts(test, 3))