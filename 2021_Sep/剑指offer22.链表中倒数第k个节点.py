class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int):
        cur = head
        n = 0
        while cur.next:
            n += 1
            cur = cur.next
        c = 0
        cur2 = head
        while c <= n - k:
            c += 1
            cur2 = cur2.next
        return cur2