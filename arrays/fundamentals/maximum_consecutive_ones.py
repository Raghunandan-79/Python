class Solution:
    def findMaxConsecutiveOnes(self, nums):
        n = len(nums)
        ones, max_ones = 0, 0

        for i in range(0, n):
            if nums[i] == 1:
                ones += 1
                max_ones = max(ones, max_ones)
            else:
                ones = 0
        
        return max_ones

def main():
    nums = list(map(int, input().split()))
    sol = Solution()
    print(sol.findMaxConsecutiveOnes(nums=nums))

if __name__ == "__main__":
    main()