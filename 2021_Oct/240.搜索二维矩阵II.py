"""
编写一个高效的算法来搜索m x n矩阵 matrix 中的一个目标值 target 。
该矩阵具有以下特性：
每行的元素从左到右升序排列。
每列的元素从上到下升序排列。
"""
"""
Z字形查找，由于矩阵的两个特性，右上角元素为最中间元素
从右上角开始，当temp过大时，则往左一位，当temp过小时，则往下一位
"""
class Solution:
    def searchMatrix(self, matrix: list, target: int):
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1
        while i < m and j >= 0:
            temp = matrix[i][j]
            if temp == target:
                return True
            elif temp > target:
                j -= 1
            else:
                i += 1
        return False

s = Solution()
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
print(s.searchMatrix(matrix, 0))