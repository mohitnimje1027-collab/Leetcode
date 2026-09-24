class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i, n in enumerate(nums):
            if sum(int(d) for d in str(n)) == i:
                return i
        return -1