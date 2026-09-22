class Solution(object):
    def resultArray(self, nums, k, queries):
        """
        :type nums: List[int]
        :type k: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(nums)
        # Find next power of 2 for optimal Segment Tree construction
        size = 1
        while size < n:
            size *= 2
        
        # Iterative Segment Tree initialization
        tree_total = [1] * (2 * size)
        tree_count = [[0] * k for _ in xrange(2 * size)]
        
        # Build base leaves
        for i in xrange(n):
            v = nums[i] % k
            tree_total[size + i] = v
            tree_count[size + i][v] = 1
            
        # Build tree upwards
        for i in xrange(size - 1, 0, -1):
            L = 2 * i
            R = 2 * i + 1
            tree_total[i] = (tree_total[L] * tree_total[R]) % k
            
            L_total = tree_total[L]
            L_count = tree_count[L]
            R_count = tree_count[R]
            
            res = list(L_count)
            for v in xrange(k):
                if R_count[v]:
                    res[(L_total * v) % k] += R_count[v]
            tree_count[i] = res
            
        ans = []
        for idx, val, start, x in queries:
            # 1. Update Phase
            p = size + idx
            val %= k
            tree_total[p] = val
            new_c = [0] * k
            new_c[val] = 1
            tree_count[p] = new_c
            
            p //= 2
            while p > 0:
                L = 2 * p
                R = 2 * p + 1
                tree_total[p] = (tree_total[L] * tree_total[R]) % k
                
                L_total = tree_total[L]
                L_count = tree_count[L]
                R_count = tree_count[R]
                
                res = list(L_count)
                for v in xrange(k):
                    if R_count[v]:
                        res[(L_total * v) % k] += R_count[v]
                tree_count[p] = res
                p //= 2
                
            # 2. Query Phase (Suffix sum from `start` to `n-1`)
            left = size + start
            right = size + n - 1
            
            res_L_total = 1
            res_L_count = [0] * k
            
            res_R_total = 1
            res_R_count = [0] * k
            
            while left <= right:
                # Merge into left accumulator block
                if left % 2 == 1:
                    new_count = list(res_L_count)
                    node_count = tree_count[left]
                    L_total = res_L_total
                    for v in xrange(k):
                        if node_count[v]:
                            new_count[(L_total * v) % k] += node_count[v]
                    res_L_count = new_count
                    res_L_total = (res_L_total * tree_total[left]) % k
                    left += 1
                    
                # Merge into right accumulator block
                if right % 2 == 0:
                    new_count = list(tree_count[right])
                    node_total = tree_total[right]
                    for v in xrange(k):
                        if res_R_count[v]:
                            new_count[(node_total * v) % k] += res_R_count[v]
                    res_R_count = new_count
                    res_R_total = (node_total * res_R_total) % k
                    right -= 1
                    
                left //= 2
                right //= 2
                
            # Merge finalizing segments L & R boundaries properly handling alignments 
            final_count = list(res_L_count)
            for v in xrange(k):
                if res_R_count[v]:
                    final_count[(res_L_total * v) % k] += res_R_count[v]
                    
            ans.append(final_count[x])
            
        return ans