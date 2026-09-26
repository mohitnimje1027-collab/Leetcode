class Solution(object):
    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """
        d = dict(knowledge)
        res = []
        i = 0
        n = len(s)
        while i < n:
            if s[i] == '(':
                j = s.index(')', i)
                key = s[i+1:j]
                res.append(d.get(key, '?'))
                i = j + 1
            else:
                res.append(s[i])
                i += 1
        return ''.join(res)