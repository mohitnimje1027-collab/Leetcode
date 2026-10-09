class Solution(object):
    def minInsertions(self, s):
        """
        :type s: int
        :rtype: int
        """
        open_count = 0
        inserts = 0
        i, n = 0, len(s)
        while i < n:
            if s[i] == '(':
                open_count += 1
                i += 1
            else:
                if i + 1 < n and s[i + 1] == ')':
                    i += 2
                else:
                    inserts += 1  # add the missing second ')'
                    i += 1
                if open_count > 0:
                    open_count -= 1
                else:
                    inserts += 1  # add a '(' to match this '))'
        return inserts + 2 * open_count
        