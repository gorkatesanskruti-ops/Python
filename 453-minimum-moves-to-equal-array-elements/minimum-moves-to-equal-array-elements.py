class Solution(object):
    def minMoves(self, nums):
        min_num = min(nums)
        return sum(nums) - len(nums) * min_num
