class Solution:
    """
    @param matrix: A lsit of lists of integers
    @return: nothing
    """
    def setZeroes(self, matrix):
        # write your code here
        # space complexity O(M + N)
        if not matrix or len(matrix) == 0:
            return
        row_marks = [False] * len(matrix)
        col_marks = [False] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row_marks[i] = True
                    col_marks[j] = True
        for i in range(len(row_marks)):
            if row_marks[i]:
                for j in range(len(matrix[0])):
                    matrix[i][j] = 0
        for j in range(len(col_marks)):
            if col_marks[j]:
                for i in range(len(matrix)):
                    matrix[i][j] = 0


sol = Solution()
matrix = [[1,2], [0,3]]
sol.setZeroes(matrix)
print(matrix)
