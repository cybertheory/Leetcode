class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        cols = set()
        rows = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    for z in range(i):
                        matrix[z][j] = 0
                    for z in range(j):
                        matrix[i][z] = 0
                    cols.add(j)
                    rows.add(i)
                elif i in rows:
                    matrix[i][j] = 0
                elif j in cols:
                    matrix[i][j] = 0
            
            