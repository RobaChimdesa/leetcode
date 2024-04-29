class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        column = len(matrix[0])
        
        Transposed_matrix = [[0] * rows for _ in range(column)]
        
        for i in range(rows):
            for j in range(column):
                print(matrix[i][j])
                Transposed_matrix[j][i] = matrix[i][j]


        return Transposed_matrix