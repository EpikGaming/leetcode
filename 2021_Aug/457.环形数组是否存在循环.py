class Solution:
    def circularArrayLoop(self, nums: list):
        n = len(nums)

        def nextNum(cur: int):
            return (cur + nums[cur]) % n


        for i, num in enumerate(nums):
            if num == 0:
                continue
            slow, fast = i, nextNum(i)
            while nums[slow] + nums[fast] > 0 and nums[slow] * nums[nextNum(fast)] > 0:
                if slow == fast:
                    if slow == nextNum(slow):
                        break
                    return True
                slow = nextNum(slow)
                fast = nextNum(nextNum(fast))
            add = i
            while nums[add] * nums[nextNum(add)] > 0:
                temp = add
                add = nextNum(add)
                nums[temp] = 0
        return False