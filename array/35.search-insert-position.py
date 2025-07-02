#
# @lc app=leetcode id=35 lang=python
#
# [35] Search Insert Position
#

# @lc code=start
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            
            if nums[i] > target:
                return i
            
            if nums[i] < target:
                if i != len(nums) - 1:
                    if target <= nums[i+1]:
                        return i + 1
                    else:
                        continue
                else:
                    return i + 1
                        

        
# @lc code=end

