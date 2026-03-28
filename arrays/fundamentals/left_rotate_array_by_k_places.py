class Solution:
    def reverseArray(self, nums, idx1, idx2):
        while idx1 < idx2:
            nums[idx1], nums[idx2] = nums[idx2], nums[idx1]
            idx1 += 1
            idx2 -= 1
    
    def rotateArray(self, nums, k) -> None:
        n = len(nums)
        k %= n

        self.reverseArray(nums, 0, k - 1)
        self.reverseArray(nums, k, n - 1)
        self.reverseArray(nums, 0, n - 1)

def main():
    nums = list(map(int, input().split()))
    k = int(input())
    sol = Solution()
    sol.rotateArray(nums=nums, k=k)
    print(nums)

if __name__ == "__main__":
    main()