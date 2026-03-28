class Solution:
    def leaders(self, nums):
        n = len(nums)
        leaders_list = []
        current_leader = nums[-1]
        leaders_list.append(current_leader)

        for i in range(n - 2, -1, -1):
            if nums[i] > current_leader:
                current_leader = nums[i]
                leaders_list.append(current_leader)
        
        leaders_list.reverse()

        return leaders_list

def main():
    nums = list(map(int, input().split()))
    sol = Solution()
    for num in sol.leaders(nums=nums):
        print(num, end=" ")
    print()

if __name__ == "__main__":
    main()