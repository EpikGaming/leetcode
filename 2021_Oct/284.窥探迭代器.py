"""
请你设计一个迭代器，除了支持hasNext和next操作外，还支持peek操作。
实现 PeekingIterator 类：
PeekingIterator(int[] nums) 使用指定整数数组 nums 初始化迭代器。
int next() 返回数组中的下一个元素，并将指针移动到下个元素处。
bool hasNext() 如果数组中存在下一个元素，返回 true ；否则，返回 false 。
int peek() 返回数组中的下一个元素，但 不 移动指针。
"""
#设计原迭代器
class Iterator:
    def __init__(self, nums: list):
        self.it = iter(nums)
        #迭代对象为nums:list[int]
        self._hasNext = None
        #判断是否有next
        self._theNext = None
        #迭代器下一个元素

    def __iter__(self):
        return self

    def next(self):
        if not self._hasNext:
            #捕捉迭代器异常
            try:
                res = next(self.it)
            except StopIteration:
                res = "iterator is empty"
        else:
            res = self._theNext
        self._hasNext = None
        return res

    def hasNext(self):
        if self._hasNext is None:
            try:
                self._theNext = next(self.it)
            except StopIteration:
                self._hasNext = False
            else:
                self._hasNext = True
        return self._hasNext


class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self._next = iterator.next()
        self._hasNext = iterator.hasNext()

    def peek(self):
        return self._next

    def hasNext(self):
        return self._hasNext

    def next(self):
        res = self._next
        self._hasNext = self.iterator.hasNext()
        self._next = self.iterator.next() if self._hasNext else None
        return res


it = PeekingIterator(Iterator([1, 3, 5]))
#Iterator类测试
test = Iterator([1, 3])
print(test.next())  # -> 1
print(test.next())  # -> 3
print(test.next())  # -> iterator is empty
print(test.next())  # -> iterator is empty
print("----------------")
#PeekingIterator类测试
while it.hasNext():
    val = it.peek()
    it.next()
    print(val)      # -> 1 3 5
print("----------------")
#PeekingIterator类方法测试
it = PeekingIterator(Iterator([1, 3, 5]))
print(it.next())    # -> 1
print(it.next())    # -> 3
print(it.peek())    # -> 5 指向下一元素5，但指针不动
print(it.next())    # -> 5 此时next仍然指向5，但指针已经移动
print(it.next())    # -> None