class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        left_rem = right_rem = 0
        for ch in s:
            if ch == '(':
                left_rem += 1
            elif ch == ')':
                if left_rem > 0:
                    left_rem -= 1
                else:
                    right_rem += 1

        res = set()
        path = []
        n = len(s)

        def dfs(i, lc, rc, lr, rr):
            if i == n:
                if lr == 0 and rr == 0 and lc == rc:
                    res.add("".join(path))
                return
            ch = s[i]
            if ch == '(':
                # remove it
                if lr > 0:
                    dfs(i + 1, lc, rc, lr - 1, rr)
                # keep it
                path.append(ch)
                dfs(i + 1, lc + 1, rc, lr, rr)
                path.pop()
            elif ch == ')':
                # remove it
                if rr > 0:
                    dfs(i + 1, lc, rc, lr, rr - 1)
                # keep it (only if it keeps the prefix valid)
                if rc < lc:
                    path.append(ch)
                    dfs(i + 1, lc, rc + 1, lr, rr)
                    path.pop()
            else:
                path.append(ch)
                dfs(i + 1, lc, rc, lr, rr)
                path.pop()

        dfs(0, 0, 0, left_rem, right_rem)
        return list(res)