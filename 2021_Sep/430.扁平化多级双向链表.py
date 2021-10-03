class ListNode:
    def __init__(self, val: int, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'ListNode'):
        def dfs(node: 'ListNode'):
            cur = node
            last = None
            while cur:
                temp = cur.next
                if cur.child:
                    child_last = dfs(cur.child)
                    temp = cur.next
                    cur.next = cur.child
                    cur.child.prev = cur

                    if temp:
                        child_last.next = temp
                        temp.prev = child_last
                    cur.child = None
                    last = child_last
                else:
                    last = cur
                cur = temp

            return last

        dfs(head)
        return head