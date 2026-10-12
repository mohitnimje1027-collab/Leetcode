from collections import deque

class Solution(object):
    def minMoves(self, classroom, energy):
        """
        :type classroom: List[str]
        :type energy: int
        :rtype: int
        """
        m, n = len(classroom), len(classroom[0])
        litter = {}
        start = None
        for i in range(m):
            for j in range(n):
                ch = classroom[i][j]
                if ch == 'S':
                    start = (i, j)
                elif ch == 'L':
                    litter[(i, j)] = len(litter)

        total = len(litter)
        if total == 0:
            return 0
        full = (1 << total) - 1

        # best[r][c][mask] = max energy seen so far at this state
        best = [[[-1] * (1 << total) for _ in range(n)] for _ in range(m)]
        sr, sc = start
        best[sr][sc][0] = energy
        q = deque([(sr, sc, 0, energy, 0)])

        while q:
            r, c, mask, e, d = q.popleft()
            if e == 0:
                continue
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if not (0 <= nr < m and 0 <= nc < n):
                    continue
                ch = classroom[nr][nc]
                if ch == 'X':
                    continue
                ne = e - 1
                nmask = mask
                if ch == 'R':
                    ne = energy
                elif ch == 'L':
                    nmask |= 1 << litter[(nr, nc)]
                if nmask == full:
                    return d + 1
                if best[nr][nc][nmask] >= ne:
                    continue
                best[nr][nc][nmask] = ne
                q.append((nr, nc, nmask, ne, d + 1))
        return -1