class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        s = nums[0]

        # Case A: rotation of sorted
        if all(nums[i] == (i + s) % n for i in range(n)):
            if s == 0:
                return 0
            return min((n - s) % n, s + 2)

        # Case B: rotation of reversed sorted
        if all(nums[i] == (s - i) % n for i in range(n)):
            sp = (s + 1) % n
            return min(1 + (n - sp) % n, sp + 1)

        return -1