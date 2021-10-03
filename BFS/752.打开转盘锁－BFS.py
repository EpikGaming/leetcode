import collections
class Solution:
    def openLock(self, deadends: list, target: str):
        if target == "0000":
            return 0

        dead = set(deadends)
        if "0000" in dead:
            return -1

        def num_prev(x: str):
            return "9" if x == "0" else str(int(x) - 1)

        def num_next(x: str):
            return "0" if x == "9" else str(int(x) + 1)

        def get(status: str):
            s = list(status)
            for i in range(4):
                temp = s[i]
                s[i] = num_prev(temp)
                yield "".join(s)
                s[i] = num_next(temp)
                yield "".join(s)
                s[i] = temp

        q = collections.deque([("0000", 0)])
        seen = {"0000"}
        while q:
            status, step = q.popleft()
            for next_status in get(status):
                if next_status not in seen and next_status not in dead:
                    if next_status == target:
                        return step + 1
                    q.append((next_status, step + 1))
                    seen.add(next_status)
        return -1


s = Solution()
deadends = ["0201", "0101", "0102", "1212", "2002"]
print(s.openLock(deadends, "0202"))