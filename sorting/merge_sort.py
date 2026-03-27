class Solution:
    def merge(self, nums, low, mid, high):
        merged = []
        left = low
        right = mid + 1

        while left <= mid and right <= high:
            if nums[left] <= nums[right]:
                merged.append(nums[left])
                left += 1
            else:
                merged.append(nums[right])
                right += 1

        while left <= mid:
            merged.append(nums[left])
            left += 1

        while right <= high:
            merged.append(nums[right])
            right += 1
        
        for i in range(low, high + 1):
            nums[i] = merged[i - low]

    def mergeSortHelper(self, nums, low, high):
        if low >= high:
            return
        
        mid = low + (high - low) // 2

        self.mergeSortHelper(nums, low, mid)
        self.mergeSortHelper(nums, mid + 1, high)
        self.merge(nums, low, mid, high)

    def mergeSort(self, nums):
        n = len(nums)
        self.mergeSortHelper(nums, 0, n - 1)
        return nums

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    sol = Solution()
    print(sol.mergeSort(nums))

if __name__ == "__main__":
    main()