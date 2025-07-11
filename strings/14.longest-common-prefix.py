#
# @lc app=leetcode id=14 lang=python
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        new_str = ""
        length = len(strs)
        if length == 0:
            return ""
        if len(strs) == 1:
            return strs[0]

        strs.sort()
        iteration = min(len(strs[0]), len(strs[length - 1]))

        for i in range(iteration):
            if strs[0][i] == strs[length-1][i]:
                new_str += strs[0][i]
            else:
                break

        return new_str

            
                
            
        
# @lc code=end