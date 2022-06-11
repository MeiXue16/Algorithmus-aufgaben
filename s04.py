class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        i, j = len(matrix)-1, 0
        while i>=0 and j<len(matrix[0]):
            flag = matrix[i][j]
            if flag >target:
                i -= 1
            elif flag <target:
                j +=1
            else: return True
        return False
