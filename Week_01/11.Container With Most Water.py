#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        i, j = 0, len(height) - 1
        while i < j:
            minHeight = min(height[i], height[j])
            res = max(res, (j - i) * minHeight)
            if height[i] < height[j]:
                i += 1 
            else:
                j -= 1
        return res


# @lc code=end