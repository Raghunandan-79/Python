class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        xor1, xor2 = 0, 0

        for i in range(0, n):
            xor1 ^= nums[i]
            xor2 ^= (i + 1)
        
        return xor1 ^ xor2

def main():
    nums = list(map(int, input().split()))
    sol = Solution()
    print(sol.missingNumber(nums=nums))

if __name__ == "__main__":
    main()