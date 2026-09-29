class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        m, n = len(grid), len(grid[0])
        if (m + n - 1) % 2 == 1:
            return False
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        # A balance above (m+n-1)//2 can never be closed, so cap it.
        limit = (m + n - 1) // 2
        cap = (1 << (limit + 1)) - 1  # keeps bits 0..limit

        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    incoming = 1  # balance 0 before the first char
                else:
                    incoming = 0
                    if i > 0:
                        incoming |= dp[i - 1][j]
                    if j > 0:
                        incoming |= dp[i][j - 1]

                if grid[i][j] == '(':
                    cur = (incoming << 1) & cap
                else:
                    cur = incoming >> 1
                dp[i][j] = cur

        return (dp[m - 1][n - 1] & 1) == 1