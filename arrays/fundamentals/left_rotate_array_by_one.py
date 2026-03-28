class Solution:
    def rotateArrayByOne(self, nums):
        n = len(nums)
        rotate_element = nums[0]

        for i in range(1, n):
            nums[i - 1] = nums[i]
        
        nums[n - 1] = rotate_element
    
def main():
    nums = list(map(int, input().split()))
    sol = Solution()
    sol.rotateArrayByOne(nums=nums)
    print(nums)

if __name__ == "__main__":
    main()