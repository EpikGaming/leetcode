"""
给你一个由非负整数a1, a2, ..., an 组成的数据流输入，
请你将到目前为止看到的数字总结为不相交的区间列表。
实现 SummaryRanges 类：
SummaryRanges() 使用一个空数据流初始化对象。
void addNum(int val) 向数据流中加入整数 val 。
int[][] getIntervals() 以不相交区间[starti, endi] 的列表形式返回对数据流中整数的总结。
"""
"""
对于进入数据流的值val，且存在两个相邻区间[l0, r0], [l1, r1]，有：
1.val 包含于区间内 l0 <= val <= r0 -> 区间集不发生变化
2.val 紧贴于一个区间的右侧 r0 + 1 == val -> 区间[l0, r0]变为[l0, val]
3.val 紧贴于一个区间的左侧 l1 - 1 == val -> 区间[l1, r1]变为[val, r1]
4.val 紧贴于两个区间的中间 r0 + 1 == val & l1 - 1 == val -> 区间[l0, r0],[l1, r1]合并为[l0, r1]
5.以上4个条件均不满足， val单独生成新区间 [val, val]
"""
from sortedcontainers import SortedDict
class SummaryRanges:
    def __init__(self):
        self.intervals = SortedDict()

    def addNum(self, val: int):
        intervals_ = self.intervals
        keys_ = self.intervals.keys()
        #keys_表示一个区间的左边界
        values_ = self.intervals.values()
        #values_表示一个区间的右边界

        #寻找最小的l1，且满足l1 > val 的区间 interval1 = [l1, r1]
        #如果不存在，则l1 == len(intervals_)
        interval1 = intervals_.bisect_right(val)

        #寻找最大的l0，且满足l0 <= val 的区间 interval0 = [l0, r0]
        #对于有序集合，设两区间相邻，有 interval0 == interval1
        interval0 = (len(intervals_) if interval1 == 0 else interval1 - 1)
        #interval0 = ("test" if interval1 == 0 else interval1 - 1)

        #print(interval0, interval1)
        #print(len(intervals_), intervals_)

        if interval0 != len(intervals_) and keys_[interval0] <= val <= values_[interval0]:
        #if interval0 != "test" and keys_[interval0] <= val <= values_[interval0]:
            #情况1
            return
        else:
            #interval0 == len(intervals_)说明interval1 == 0，即不存在interval0[l0, r0]
            left_side = (interval0 != len(intervals_) and val == values_[interval0] + 1)
            #left_side = (interval0 != "test" and val == values_[interval0] + 1)

            #interval1 == len(intervals_)说明不存在interval1[l1, r1]
            right_side = (interval1 != len(intervals_) and val == keys_[interval1] - 1)

            if left_side and right_side:
                #情况4
                left, right = keys_[interval0], values_[interval1]
                intervals_.popitem(interval1)
                intervals_.popitem(interval0)
                intervals_[left] = right
            elif left_side:
                #情况2
                #right = values_[interval0] = intervals_[keys_[interval0]]
                #right += 1
                intervals_[keys_[interval0]] += 1
            elif right_side:
                #情况3
                right = values_[interval1]
                intervals_.popitem(interval1)
                intervals_[val] = right
            else:
                #情况5
                intervals_[val] = val

    def getIntervals(self):
        return list(self.intervals.items())

s = SummaryRanges()
s.addNum(1)
print(s.getIntervals())  # -> [(1, 1)]
s.addNum(3)
print(s.getIntervals())  # -> [(1, 1), (3, 3)]
s.addNum(7)
print(s.getIntervals())  # -> [(1, 1), (3, 3), (7, 7)]
s.addNum(2)
print(s.getIntervals())  # -> [(1, 3), (7, 7)]
s.addNum(6)
print(s.getIntervals())  # -> [(1, 3), (6, 7)]