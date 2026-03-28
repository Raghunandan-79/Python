class Solution:
    def spiralOrder(self, matrix):
        n, m = len(matrix), len(matrix[0])
        ans = []
        top, bottom = 0, n - 1
        left, right = 0, m - 1

        while (top <= bottom) and (left <= right):
            # left to right
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
            top += 1

            # top to bottom
            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            right -= 1

            # right to left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    ans.append(matrix[bottom][i])
                bottom -= 1
        
            # bottom to top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])
                left += 1
        
        return ans

def main():
    matrix = []
    n, m = map(int, input().split())
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    sol = Solution()
    for num in sol.spiralOrder(matrix=matrix):
        print(num, end=" ")
    print()

if __name__ == "__main__":
    main()