class Solution:
    def isMatch(self, s, p):
        i = 0          # Pointer for s
        j = 0          # Pointer for p

        star = -1      # Position of last '*'
        match = 0      # Position in s when '*' was found

        while i < len(s):

            # Case 1: Characters match or pattern has '?'
            if j < len(p) and (p[j] == s[i] or p[j] == '?'):
                i += 1
                j += 1

            # Case 2: Pattern has '*'
            elif j < len(p) and p[j] == '*':
                star = j
                match = i
                j += 1

            # Case 3: Previous '*' can match more characters
            elif star != -1:
                j = star + 1
                match += 1
                i = match

            # Case 4: No match
            else:
                return False

        # Remaining characters in pattern must all be '*'
        while j < len(p) and p[j] == '*':
            j += 1

        return j == len(p)