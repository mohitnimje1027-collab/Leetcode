class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i, j = 0, len(nums) - 1
        total = 0
        while i < j:
            total += nums[j] - nums[i]
            i += 1
            j -= 1
        return total