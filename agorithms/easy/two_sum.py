from typing import List


# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for index, item in enumerate(nums):
            if target - item in my_dict:
                return [my_dict[target - item], index]
            my_dict[item] = index
