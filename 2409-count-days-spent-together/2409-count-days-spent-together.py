class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        """
        :type arriveAlice: str
        :type leaveAlice: str
        :type arriveBob: str
        :type leaveBob: str
        :rtype: int
        """
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        pref = [0]
        for d in days:
            pref.append(pref[-1] + d)

        def to_day(date):
            m, d = int(date[:2]), int(date[3:])
            return pref[m - 1] + d

        start = max(to_day(arriveAlice), to_day(arriveBob))
        end = min(to_day(leaveAlice), to_day(leaveBob))
        return max(0, end - start + 1)