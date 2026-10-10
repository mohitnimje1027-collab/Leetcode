class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k1: int
        :type k2: int
        :rtype: int
        """
        k = k1 + k2
        n = len(nums1)
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        if sum(diffs) <= k:
            return 0

        mx = max(diffs)
        count = [0] * (mx + 1)
        for d in diffs:
            count[d] += 1

        cnt = 0  # elements currently at level v (after flattening)
        v = mx
        while v > 0:
            cnt += count[v]
            count[v] = 0
            if cnt > 0:
                if k >= cnt:
                    # lower all cnt elements from v to v-1
                    k -= cnt
                    # they join level v-1
                    # (cnt carries over to next iteration)
                else:
                    # can't lower all; k of them go to v-1, rest stay at v
                    count[v] = cnt - k
                    count[v - 1] += k
                    k = 0
                    cnt = 0
                    break
            v -= 1
        else:
            # reached level 0 with all flattened elements; they sit at 0
            pass

        if cnt > 0 and v == 0:
            count[0] += cnt

        return sum(val * val * c for val, c in enumerate(count))