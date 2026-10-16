class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)
        s = [0] * (4 * n)   # sum of d over node range
        q = [0] * (4 * n)   # sum of d^2 over node range
        lz = [0] * (4 * n)  # pending add

        def apply(o, length, a):
            q[o] += 2 * a * s[o] + a * a * length
            s[o] += a * length
            lz[o] += a

        def update(o, l, r, ql, qr):
            if ql <= l and r <= qr:
                apply(o, r - l + 1, 1)
                return
            m = (l + r) // 2
            if lz[o]:
                apply(2 * o, m - l + 1, lz[o])
                apply(2 * o + 1, r - m, lz[o])
                lz[o] = 0
            if ql <= m:
                update(2 * o, l, m, ql, qr)
            if qr > m:
                update(2 * o + 1, m + 1, r, ql, qr)
            s[o] = s[2 * o] + s[2 * o + 1]
            q[o] = q[2 * o] + q[2 * o + 1]

        last = {}
        ans = 0
        for j, x in enumerate(nums):
            p = last.get(x, -1)
            update(1, 0, n - 1, p + 1, j)
            last[x] = j
            ans += q[1]
        return ans % MOD