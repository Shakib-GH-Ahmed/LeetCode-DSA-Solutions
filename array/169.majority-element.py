#
# @lc app=leetcode id=169 lang=python
#
# [169] Majority Element
#

# @lc code=start
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        track = {}
        majority_val = 0
        majority_key = None
        

        for i in nums:
            if i not in track:
                track[i] = 1
            else:
                track[i] += 1
        
        for key,value in track.items():
            if value > majority_val:
                majority_val = value
                majority_key = key
        
        return majority_key
        
        
# @lc code=end

