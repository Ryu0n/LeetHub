import math

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = list()
        while len(nums1) > 0 or len(nums2) > 0:
            if len(nums1) == 0:
                merged.append(nums2.pop(0))
                continue
            if len(nums2) == 0:
                merged.append(nums1.pop(0))
                continue
            if nums1[0] > nums2[0]:
                n2 = nums2.pop(0)
                merged.append(n2)
            elif nums1[0] < nums2[0]:
                n1 = nums1.pop(0)
                merged.append(n1)
            else:
                n1 = nums1.pop(0)
                n2 = nums2.pop(0)
                merged.extend([n1, n2])
        
        c = len(merged)//2
        if len(merged) % 2 == 0:
            return (merged[c] + merged[c-1])/2
        return merged[c]


        