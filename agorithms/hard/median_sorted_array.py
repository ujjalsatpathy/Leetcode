from typing import List


# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        joined_list = sorted(nums1 + nums2)
        length = int(len(joined_list)/2)

        if len(joined_list)%2 == 0:
            first = joined_list[length]
            second = joined_list[length-1]
            return (first+second)/2
        else:
            return joined_list[length]

