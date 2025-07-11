#
# @lc app=leetcode id=643 lang=python
#
# [643] Maximum Average Subarray I
#

# @lc code=start
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        maxSum = float('-inf')
        currentSum = 0
        start = 0
        end = k 

        for i in range(start, end):
            currentSum += nums[i]
        
        if currentSum > maxSum:
            maxSum = currentSum

        while end < len(nums):
            currentSum = currentSum - nums[start] + nums[end]
            if currentSum > maxSum:
                maxSum = currentSum
            
            start += 1
            end += 1

        maxAVG = float(maxSum) / k
        return maxAVG
    
# @lc code=end

