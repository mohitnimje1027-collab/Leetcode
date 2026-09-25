class Solution(object):
    def braceExpansionII(self, expression):
        """
        :type expression: str
        :rtype: List[str]
        """
        s = expression
        self.i = 0
        n = len(s)
        
        def parseUnion():
            # Parses a comma-separated list of concatenation terms, unions their results
            result = parseConcat()
            while self.i < n and s[self.i] == ',':
                self.i += 1  # skip ','
                result |= parseConcat()
            return result
        
        def parseConcat():
            # Parses a sequence of factors concatenated together
            result = {""}
            while self.i < n and s[self.i] not in ',}':
                factor = parseFactor()
                result = {a + b for a in result for b in factor}
            return result
        
        def parseFactor():
            if s[self.i] == '{':
                self.i += 1  # skip '{'
                result = parseUnion()
                self.i += 1  # skip '}'
                return result
            else:
                # single lowercase letter
                result = {s[self.i]}
                self.i += 1
                return result
        
        final_set = parseUnion()
        return sorted(final_set)