class Solution:
    def isNumber(self, s):
        digit = False
        dot = False
        exp = False
        exp_digit = True

        for i, ch in enumerate(s):
            if ch.isdigit():
                digit = True
                if exp:
                    exp_digit = True

            elif ch == '.':
                if dot or exp:
                    return False
                dot = True

            elif ch == 'e' or ch == 'E':
                if exp or not digit:
                    return False
                exp = True
                exp_digit = False

            elif ch == '+' or ch == '-':
                if i != 0 and s[i - 1] not in ('e', 'E'):
                    return False

            else:
                return False

        return digit and exp_digit