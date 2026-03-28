class Solution:
    def unionArray(self, nums1, nums2):
        n1, n2 = len(nums1), len(nums2)
        i, j = 0, 0
        union = []

        while i < n1 and j < n2:
            if nums1[i] <= nums2[j]:
                if not union or union[-1] != nums1[i]:
                    union.append(nums1[i])
                i += 1
            else:
                if not union or union[-1] != nums2[j]:
                    union.append(nums2[j])
                j += 1
        
        while i < n1:
            if not union or union[-1] != nums1[i]:
                union.append(nums1[i])
            i += 1

        while j < n2:
            if not union or union[-1] != nums2[j]:
                union.append(nums2[j])
            j += 1
        
        return union

def main():
    nums1 = list(map(int, input().split()))
    nums2 = list(map(int, input().split()))
    nums1.sort()
    nums2.sort()
    sol = Solution()
    result = sol.unionArray(nums1=nums1, nums2=nums2)
    print(result)

if __name__ == "__main__":
    main()