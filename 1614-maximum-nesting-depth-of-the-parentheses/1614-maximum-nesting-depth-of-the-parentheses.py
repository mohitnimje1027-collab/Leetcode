class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        depth = 0
        best = 0
        for ch in s:
            if ch == '(':
                depth += 1
                if depth > best:
                    best = depth
            elif ch == ')':
                depth -= 1
        return best