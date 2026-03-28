class Solution:
    def rearrangeArray(self, nums):
        n = len(nums)
        positive_index = 0
        negative_index = 1
        ans = [0] * n

        for i in range(n):
            if nums[i] > 0:
                ans[positive_index] = nums[i]
                positive_index += 2
            else:
                ans[negative_index] = nums[i]
                negative_index += 2
        
        return ans

def main():
    nums = list(map(int, input().split()))
    sol = Solution()
    for num in sol.rearrangeArray(nums=nums):
        print(num, end=" ")
    print()

if __name__ == "__main__":
    main()
