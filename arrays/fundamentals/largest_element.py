class Solution:
    def largestElement(self, nums):
        n = len(nums)
        largest = nums[0]

        for i in range(1, n):
            if nums[i] > largest:
                largest = nums[i]
        
        return largest

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    sol = Solution()
    print(sol.largestElement(nums))

if __name__ == "__main__":
    main()