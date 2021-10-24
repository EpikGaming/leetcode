"""
作为一位web开发者， 懂得怎样去规划一个页面的尺寸是很重要的。
现给定一个具体的矩形页面面积，你的任务是设计一个长度为 L 和宽度为 W 且满足以下要求的矩形的页面。要求：
1. 你设计的矩形页面必须等于给定的目标面积。
2. 宽度 W 不应大于长度 L，换言之，要求 L >= W 。
3. 长度 L 和宽度 W 之间的差距应当尽可能小。
你需要按顺序输出你设计的页面的长度 L 和宽度 W。
"""
"""
当矩阵的长宽最接近时 -> 矩阵变成正方形
从面积的开根号temp开始到1,如果area % i == 0,说明构成矩阵,同时也是长宽差值最小的
此时直接返回[area // i, i]
"""
class Solution:
    def constructRectangle(self, area: int):
        res = []
        temp = int(area ** 0.5)
        for i in range(temp, 0, -1):
            if area % i == 0:
                return [area // i, i]
        return res


s = Solution()
print(s.constructRectangle(10))