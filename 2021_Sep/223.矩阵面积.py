class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int):
        A = (ax2 - ax1) * (ay2 - ay1)
        B = (bx2 - bx1) * (by2 - by1)
        overL = min(ax2, bx2) - max(ax1, bx1)
        overW = min(ay2, by2) - max(ay1, by1)
        C = max(overW, 0) * max(overL, 0)
        return A + B - C


