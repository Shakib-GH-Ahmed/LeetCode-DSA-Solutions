#
# @lc app=leetcode id=283 lang=python
#
# [283] Move Zeroes
#

# @lc code=start
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        idx = 0
        if len(nums) == 1:
            return nums

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[idx] = nums[i]
                idx += 1
        
        for i in range(idx, len(nums)):
            nums[i] = 0
        
        return nums
                
        
# @lc code=end

