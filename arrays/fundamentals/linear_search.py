class Solution:
    def linearSearch(self, nums, x):
        n = len(nums)

        for i in range(0, n):
            if nums[i] == x:
                return i

        return -1
    
def main():
    n = int(input())
    nums = list(map(int, input().split()))
    x = int(input())
    sol = Solution()
    print(sol.linearSearch(nums, x))

if __name__ == "__main__":
    main()