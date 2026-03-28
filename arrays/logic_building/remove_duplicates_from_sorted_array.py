class Solution:
    def removeDuplicates(self, nums):
        n = len(nums)
        i = 0

        for j in range(1, n):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        
        return i + 1

def main():
    nums = list(map(int, input().split()))
    sol = Solution()
    k = sol.removeDuplicates(nums=nums)
    for i in range(k):
        print(nums[i], end=" ")
    print()

if __name__ == "__main__":
    main()