class Solution:
    def secondLargestElement(self, nums):
        n = len(nums)
        largest, second_largest = float("-inf"), float("-inf")

        for i in range(0, n):
            if nums[i] > largest:
                second_largest = largest
                largest = nums[i]
            elif nums[i] > second_largest and nums[i] != largest:
                second_largest = nums[i]
        
        return second_largest if second_largest != float("-inf") else -1

def main():
    nums = list(map(int, input().split()))
    sol = Solution()
    print(sol.secondLargestElement(nums))

if __name__ == "__main__":
    main()