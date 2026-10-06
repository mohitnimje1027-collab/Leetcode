class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        open_count = 0
        moves = 0
        for ch in s:
            if ch == '(':
                open_count += 1
            elif open_count > 0:
                open_count -= 1
            else:
                moves += 1
        return moves + open_count