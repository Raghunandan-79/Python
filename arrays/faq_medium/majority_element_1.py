class Solution:
    def majorityElement(self, nums):
        n = len(nums)
        el, cnt = 0, 0

        for i in range(n):
            if cnt == 0:
                el = nums[i]
                cnt = 1
            elif el == nums[i]:
                cnt += 1
            else:
                cnt -= 1
        
        cnt1 = 0
        for num in nums:
            if num == el:
                cnt1 += 1
        
        return el if cnt1 > (n // 2) else -1

def main():
    nums = list(map(int, input().split()))
    sol = Solution()
    print(sol.majorityElement(nums=nums))

if __name__ == "__main__":
    main()