class Solution(object):
    def palindromePath(self, n, edges, s, queries):
        """
        :type n: int
        :type edges: List[List[int]]
        :type s: str
        :type queries: List[str]
        :rtype: List[bool]
        """
        s = list(s)
        bit = lambda ch: 1 << (ord(ch) - 97)

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        LOG = max(1, (n).bit_length())
        parent = [0] * n
        depth = [0] * n
        base = [0] * n          # initial root-to-node XOR
        tin = [0] * n
        order = []
        base[0] = bit(s[0])
        stack = [0]
        parent[0] = 0
        seen_root = True
        while stack:
            v = stack.pop()
            order.append(v)
            tin[v] = len(order)          # 1-indexed for the BIT
            for w in adj[v]:
                if w != parent[v] or (v == 0 and w != 0 and w not in ()):
                    if w == parent[v] and v != 0:
                        continue
                    if v == 0 and w == parent[0] and w == 0:
                        continue
                    parent[w] = v
                    depth[w] = depth[v] + 1
                    base[w] = base[v] ^ bit(s[w])
                    stack.append(w)

        size = [1] * n
        for v in reversed(order):
            if v != 0:
                size[parent[v]] += size[v]

        up = [parent[:]]
        for j in range(1, LOG):
            prev = up[-1]
            up.append([prev[prev[v]] for v in range(n)])

        def lca(a, b):
            if depth[a] < depth[b]:
                a, b = b, a
            diff = depth[a] - depth[b]
            for j in range(LOG):
                if (diff >> j) & 1:
                    a = up[j][a]
            if a == b:
                return a
            for j in range(LOG - 1, -1, -1):
                if up[j][a] != up[j][b]:
                    a = up[j][a]
                    b = up[j][b]
            return up[0][a]

        tree = [0] * (n + 2)

        def bit_xor(i, x):
            while i <= n + 1:
                tree[i] ^= x
                i += i & -i

        def bit_query(i):
            r = 0
            while i > 0:
                r ^= tree[i]
                i -= i & -i
            return r

        def prefix(v):
            return base[v] ^ bit_query(tin[v])

        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u, c = int(parts[1]), parts[2]
                d = bit(s[u]) ^ bit(c)
                if d:
                    bit_xor(tin[u], d)
                    bit_xor(tin[u] + size[u], d)
                    s[u] = c
            else:
                u, v = int(parts[1]), int(parts[2])
                l = lca(u, v)
                mask = prefix(u) ^ prefix(v) ^ bit(s[l])
                ans.append(mask & (mask - 1) == 0)
        return ans