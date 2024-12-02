import math
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sa = sorted(nums1 + nums2)
        length = len(sa)
        if length % 2 == 0:
            return (sa[length // 2] + sa[(length // 2) - 1]) / 2

        return sa[math.floor(length / 2)]


s = Solution()
s.findMedianSortedArrays([1,3], [2])
