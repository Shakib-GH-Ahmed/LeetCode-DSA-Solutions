#
# @lc app=leetcode id=13 lang=python
#
# [13] Roman to Integer
#

# @lc code=start
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        total_val = 0
        last_val = 0
        for symbol in reversed(s):
            value = roman[symbol]
            if value < last_val:
                total_val -= value
            else:
                total_val += value

            last_val = value

        return total_val

# @lc code=end

