class Solution(object):
    def sortableIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # pref[i] = number of descents among positions 0..i-1 (nums[p] > nums[p+1])
        pref = [0] * n
        for i in range(n - 1):
            pref[i + 1] = pref[i] + (1 if nums[i] > nums[i + 1] else 0)

        total = 0
        for k in range(1, n + 1):
            if n % k:
                continue
            ok = True
            prev_max = 0
            for s in range(0, n, k):
                e = s + k - 1
                desc = pref[e] - pref[s]          # descents inside the block
                if nums[e] > nums[s]:             # wrap-around descent
                    desc += 1
                if desc > 1:
                    ok = False
                    break
                block = nums[s:e + 1]
                if min(block) < prev_max:
                    ok = False
                    break
                prev_max = max(block)
            if ok:
                total += k
        return total