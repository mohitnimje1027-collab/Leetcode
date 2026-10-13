class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sq = sorted(x * x for x in nums)
        h = len(nums) // 2
        return sum(sq[h:]) - sum(sq[:h])