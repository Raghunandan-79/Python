class Solution:
    def rotateMatrix(self, matrix):
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(len(matrix)):
            matrix[i].reverse()
    
def main():
    matrix = []
    n, m = map(int, input().split())
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    sol = Solution()
    sol.rotateMatrix(matrix=matrix)
    for row in matrix:
        print(row)

if __name__ == "__main__":
    main()