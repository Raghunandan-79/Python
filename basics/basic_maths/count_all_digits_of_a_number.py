class Solution:
    def countDigits(self, n):
        if n == 0:
            return 1

        cnt = 0
        while n > 0:
            cnt += 1
            n //= 10
        
        return cnt

def main():
    n = int(input())
    sol = Solution()
    print(sol.countDigits(n))

if __name__ == "__main__":
    main()