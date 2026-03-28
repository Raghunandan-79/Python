class Solution:
    def moveZeros(self, nums):
        n = len(nums)
        j = 0

        for i in range(n):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

def main():
    nums = list(map(int, input().split()))
    sol = Solution()
    sol.moveZeros(nums)
    print(nums)

if __name__ == "__main__":
    main()