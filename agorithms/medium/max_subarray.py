# Given an integer array nums, find the subarray with the largest sum, and return its sum.
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = max_sum = nums[0]
        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)
        return max_sum

cls = Solution()
print(cls.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

# Thendialarasan
