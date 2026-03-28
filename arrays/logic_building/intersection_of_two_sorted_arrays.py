class Solution:
    def intersectionArray(self, nums1, nums2):
        n1, n2 = len(nums1), len(nums2)
        i, j = 0, 0
        intersection = []

        while i < n1 and j < n2:
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                intersection.append(nums1[i])
                i += 1
                j += 1
        
        return intersection

def main():
    nums1 = list(map(int, input().split()))
    nums2 = list(map(int, input().split()))
    nums1.sort()
    nums2.sort()
    sol = Solution()
    print(sol.intersectionArray(nums1=nums1, nums2=nums2))

if __name__ == "__main__":
    main()