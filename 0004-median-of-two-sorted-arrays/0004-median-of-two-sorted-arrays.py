class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        
        total = len(nums1) + len(nums2)
        half = (total + 1) // 2

        left = 0
        right = len(nums1)

        while left <= right:

            i = (right + left) // 2
            j = half - i

            L1 = nums1[i - 1] if i > 0 else float('-inf')
            R1 = nums1[i] if i < len(nums1) else float('inf')
            L2 = nums2[j - 1] if j > 0 else float('-inf')
            R2 = nums2[j] if j < len(nums2) else float('inf')

            if L1 > R2:
                right = i - 1
            elif L2 > R1:
                left = i + 1
            else:
                if total % 2 == 1:
                    return max(L1,L2)
                else:
                    return (min(R1,R2) + max(L1, L2)) / 2
