#
# @lc app=leetcode id=28 lang=python
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        flag = False
        occurance_idx = []
        if needle == "":
            return 0

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i: i + len(needle)] == needle:
                occurance_idx.append(i)
                flag = True

        return occurance_idx[0] if flag == True else -1
        
        
# @lc code=end

