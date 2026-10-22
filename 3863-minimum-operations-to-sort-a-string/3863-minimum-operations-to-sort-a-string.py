class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        t = sorted(s)
        if list(s) == t:
            return 0
        if n == 2:
            return -1
        mn, mx = t[0], t[-1]
        if s[0] == mn or s[-1] == mx:
            return 1
        # min occurs somewhere other than the last position,
        # or max occurs somewhere other than the first position
        if mn in s[:-1] or mx in s[1:]:
            return 2
        return 3